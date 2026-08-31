document.addEventListener('DOMContentLoaded', function () {
  const fiberProfiles = {
    om3: { name: 'OM3 MMF', attenuation: { 850: 3.0, 1300: 1.5 }, connector: 0.75, splice: 0.1, patch: 0.35 },
    om4: { name: 'OM4 MMF', attenuation: { 850: 2.8, 1300: 1.5 }, connector: 0.75, splice: 0.1, patch: 0.35 },
    os2: { name: 'OS2 SMF', attenuation: { 1310: 0.4, 1550: 0.25 }, connector: 0.5, splice: 0.1, patch: 0.35 }
  };

  const opticalProfiles = {
    '100g-sr4': { label: '100GBASE-SR4', family: '100G', wavelength: 850, fiber: 'om4', txPower: -4, rxSensitivity: -9.5, opticalBudget: 5.5, note: 'MMF short-range, often used in data-center links.' },
    '100g-lr4': { label: '100GBASE-LR4', family: '100G', wavelength: 1310, fiber: 'os2', txPower: -3, rxSensitivity: -13.5, opticalBudget: 10.5, note: 'SMF long-range, suitable for campus or point-to-point links.' },
    '200g-dr4': { label: '200GBASE-DR4', family: '200G', wavelength: 1310, fiber: 'os2', txPower: -1, rxSensitivity: -11.0, opticalBudget: 10.0, note: 'SMF short-to-medium reach, commonly used in modern DC fabrics.' },
    '400g-dr4': { label: '400GBASE-DR4', family: '400G', wavelength: 1310, fiber: 'os2', txPower: 0, rxSensitivity: -11.5, opticalBudget: 11.5, note: 'SMF, strong fit for dense short-haul designs.' },
    '400g-sr8': { label: '400GBASE-SR8', family: '400G', wavelength: 850, fiber: 'om4', txPower: -4, rxSensitivity: -9.5, opticalBudget: 5.5, note: 'MMF short-reach, usually best for very short DC links.' },
    '800g-dr8': { label: '800GBASE-DR8', family: '800G', wavelength: 1310, fiber: 'os2', txPower: 0, rxSensitivity: -11.0, opticalBudget: 11.0, note: 'High-speed short/medium reach for dense data-center or metro-style links.' }
  };

  function computeLinkLoss(lengthKm, fiberType, wavelength, connectors, splices, patchLeads, safetyMargin) {
    const profile = fiberProfiles[fiberType];
    if (!profile) return null;
    const attenuation = profile.attenuation[wavelength] ?? Object.values(profile.attenuation)[0];
    const totalLoss = (lengthKm * attenuation) + (connectors * profile.connector) + (splices * profile.splice) + (patchLeads * profile.patch) + safetyMargin;
    return { totalLoss, attenuation, connectorLoss: profile.connector, spliceLoss: profile.splice, patchLoss: profile.patch };
  }

  function setResultState(element, state, text) {
    element.className = 'result ' + state;
    element.textContent = text;
  }

  function basicCalculator() {
    const form = document.getElementById('basic-loss-form');
    if (!form) return;

    const lengthInput = document.getElementById('basic-length');
    const fiberTypeSelect = document.getElementById('basic-fiber');
    const wavelengthSelect = document.getElementById('basic-wavelength');
    const connectorsInput = document.getElementById('basic-connectors');
    const splicesInput = document.getElementById('basic-splices');
    const patchLeadsInput = document.getElementById('basic-patch-leads');
    const marginInput = document.getElementById('basic-margin');
    const txInput = document.getElementById('basic-tx-power');
    const rxInput = document.getElementById('basic-rx-sensitivity');
    const resultBox = document.getElementById('basic-result');

    function update() {
      const lengthMeters = Number(lengthInput.value) || 0;
      const lengthKm = lengthMeters / 1000;
      const fiberType = fiberTypeSelect.value;
      const wavelength = Number(wavelengthSelect.value);
      const connectors = Number(connectorsInput.value) || 0;
      const splices = Number(splicesInput.value) || 0;
      const patchLeads = Number(patchLeadsInput.value) || 0;
      const safetyMargin = Number(marginInput.value) || 0;
      const txPower = Number(txInput.value) || 0;
      const rxSensitivity = Number(rxInput.value) || 0;

      const result = computeLinkLoss(lengthKm, fiberType, wavelength, connectors, splices, patchLeads, safetyMargin);
      if (!result) {
        setResultState(resultBox, 'warning', 'Choose a valid fiber type.');
        return;
      }

      const linkMargin = (txPower - rxSensitivity) - result.totalLoss;
      const status = linkMargin >= 0 ? 'ok' : 'warning';
      const statusText = linkMargin >= 0 ? 'Link is within optical budget.' : 'Link is above the optical budget and may need design changes.';
      const detail = `Total loss: ${result.totalLoss.toFixed(2)} dB | Link margin: ${linkMargin.toFixed(2)} dB`;
      setResultState(resultBox, status, `${statusText} ${detail}`);
    }

    form.addEventListener('input', update);
    form.addEventListener('change', update);
    update();
  }

  function highSpeedCalculator() {
    const form = document.getElementById('high-speed-form');
    if (!form) return;

    const opticsSelect = document.getElementById('optics-profile');
    const fiberTypeSelect = document.getElementById('hs-fiber');
    const lengthInput = document.getElementById('hs-length');
    const connectorsInput = document.getElementById('hs-connectors');
    const splicesInput = document.getElementById('hs-splices');
    const patchLeadsInput = document.getElementById('hs-patch-leads');
    const marginInput = document.getElementById('hs-margin');
    const txValue = document.getElementById('hs-tx-power');
    const rxValue = document.getElementById('hs-rx-sensitivity');
    const profileDescription = document.getElementById('optics-profile-note');
    const resultBox = document.getElementById('high-speed-result');

    function updateOpticsMeta() {
      const profile = opticalProfiles[opticsSelect.value];
      if (!profile) return;

      const fiber = fiberProfiles[profile.fiber];
      const wavelengths = Object.keys(fiber.attenuation).map(Number).sort((a, b) => a - b);
      const wavelengthsText = wavelengths.join(', ') + ' nm';
      txValue.value = profile.txPower;
      rxValue.value = profile.rxSensitivity;

      profileDescription.textContent = `${profile.label} • typical optical budget ${profile.opticalBudget} dB • common wavelengths: ${wavelengthsText} • ${profile.note}`;
    }

    function update() {
      const profile = opticalProfiles[opticsSelect.value];
      if (!profile) {
        setResultState(resultBox, 'warning', 'Choose an optics profile.');
        return;
      }

      const fiberType = fiberTypeSelect.value;
      const lengthMeters = Number(lengthInput.value) || 0;
      const lengthKm = lengthMeters / 1000;
      const connectors = Number(connectorsInput.value) || 0;
      const splices = Number(splicesInput.value) || 0;
      const patchLeads = Number(patchLeadsInput.value) || 0;
      const safetyMargin = Number(marginInput.value) || 0;
      const txPower = Number(txValue.value) || 0;
      const rxSensitivity = Number(rxValue.value) || 0;

      const result = computeLinkLoss(lengthKm, fiberType, profile.wavelength, connectors, splices, patchLeads, safetyMargin);
      if (!result) {
        setResultState(resultBox, 'warning', 'Choose a valid fiber type.');
        return;
      }

      const linkMargin = (txPower - rxSensitivity) - result.totalLoss;
      const status = linkMargin >= 0 ? 'ok' : 'warning';
      const statusText = linkMargin >= 0 ? 'This optics profile remains within the operating window for the planned link.' : 'This link is likely too lossy for the selected optics and needs design review.';
      const detail = `Total loss: ${result.totalLoss.toFixed(2)} dB | Link margin: ${linkMargin.toFixed(2)} dB | Optical budget: ${profile.opticalBudget.toFixed(1)} dB`;
      setResultState(resultBox, status, `${statusText} ${detail}`);
    }

    opticsSelect.addEventListener('change', updateOpticsMeta);
    opticsSelect.addEventListener('change', update);
    fiberTypeSelect.addEventListener('change', update);
    form.addEventListener('input', update);
    form.addEventListener('change', update);
    updateOpticsMeta();
    update();
  }

  basicCalculator();
  highSpeedCalculator();
});

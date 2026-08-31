---
name: "Jekyll blog drafting and approval-gated publishing"
description: "Create blog posts for this Jekyll repository in a local branch, align them with the existing site structure, keep the draft iterative, and only publish after explicit user approval."
---

# Jekyll blog drafting and approval-gated publishing

This repository is a Jekyll-based personal blog. The workflow here is intentionally conservative: content should be drafted locally, reviewed iteratively, and published only after explicit approval.

## Scope

This skill applies only to this repository and its established patterns. It is not a generic blog-writing skill.

Use the existing conventions in:
- [_config.yml](_config.yml)
- [index.md](index.md)
- existing posts in [_posts/](_posts)
- topic/data scripts in [scripts/](scripts)

## Core workflow

1. Inspect the repo conventions before writing
   - Check the site configuration in [_config.yml](_config.yml)
   - Match the style and front matter used by recent posts in [_posts/](_posts)
   - Confirm topic/category alignment with the site layout and homepage

2. Create a local feature branch before editing
   - Keep the draft isolated from the main branch while it is still being refined
   - Do not merge or push a draft to the public branch before the user approves the content
   - If the repository convention expects a PR, follow that path rather than merging locally without review

3. Draft a post in the correct location
   - Add a new file under [_posts/](_posts) using the repo’s naming conventions
   - Include appropriate front matter: title, date, categories, excerpt, and layout
   - Keep the article structure consistent with existing site posts

4. Keep the draft iterative and local
   - This process may take multiple passes while the user refines wording, structure, and claims
   - Save progress locally; do not assume the first draft is final
   - Do not push, open a pull request, or merge during the drafting phase unless explicitly requested

5. Validate the draft before presenting it for approval
   - Run a local Jekyll build and check for errors
   - Check formatting, metadata, category alignment, links, and filenames
   - Verify it fits the site’s topic structure and content style
   - If a topic or category is new, update the site configuration and homepage logic as needed
   - Review image backgrounds, figure sizing, and mobile readability for critical visuals

6. Ask for approval before publishing
   - Summarize what was created and what changed
   - Highlight any follow-up decisions needed from the user
   - Wait for explicit user approval before any push, PR, or merge

7. Publish only after approval
   - Push the approved local branch when the repo workflow requires it
   - Open or update a pull request if the workflow requires it
   - Merge to the default branch only after the user confirms it is ready to go live
   - If the remote branch is ahead, sync or rebase before pushing

8. Verify the live result after publication
   - Build locally and confirm the generated output file exists under [_site/](_site)
   - Check the public permalink format from the repo configuration
   - Confirm the final URL responds successfully before saying it is live
   - Do not assume the browser-visible title and the generated URL are the same thing

## Safety rules

- Never publish or merge automatically during the drafting phase.
- Never push a draft to GitHub without explicit user approval.
- Keep changes limited to the intended post or related repo conventions.
- Do not expose secrets, tokens, private accounts, or personal deployment details in a public repo skill.
- Prefer repo-scoped, project-safe instructions over personal workflow preferences.
- Treat the repo’s published URL pattern as a required validation step, not as an optional check.

## Safety rules

- Never publish or merge automatically during the drafting phase.
- Never push a draft to GitHub without explicit user approval.
- Keep changes limited to the intended post or related repo conventions.
- Do not expose secrets, tokens, private accounts, or personal deployment details in a public repo skill.
- Prefer repo-scoped, project-safe instructions over personal workflow preferences.

## Repo-specific conventions

- Use the existing Jekyll front matter pattern seen in current posts.
- Match the site’s topic names and categories when relevant.
- Preserve the repo’s site structure and permalink behavior.
- If a draft depends on generated content or data-fetch scripts, validate that the data source and output remain consistent with the repo.

## Replace or retire this skill

This skill is intended to be updated or replaced if the project workflow changes. If a newer or more specific skill is created, prefer the most relevant active skill and retire this one cleanly.

## Example prompts this skill supports

- Create a new post about AI governance and draft it locally on a feature branch.
- Draft a new quantum topic post that matches the existing Jekyll structure and wait for my review before publishing.
- Update this blog with a new post, but keep the draft local until I approve it.
- Review my draft post against the repo’s existing style and site conventions before I decide to publish.

## Completion criteria

The workflow is complete only when:
- a local draft exists on a feature branch
- the content matches the repo’s structure and conventions
- the user has reviewed and approved it
- and the site is published only after that approval

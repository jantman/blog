# Features

This directory contains markdown files describing features that we want to implement for this project. Each feature initially just includes a human-generated explanation; for each feature you (Claude Code, the AI coding assistant) will update that document to include an implementation plan to resolve the feature and then await human approval before proceeding. You are encouraged to solicit human input/feedback during the planning phase for anything you have questions about or do not feel is clear. After planning, you MUST update the feature document with your implementation plan and commit it to git. Once planning is complete, if you get confused or are unable to accomplish a feature without significant issues, please ask for human feedback. You MUST plan one feature at a time, in order, and then implement that feature. As earlier features may inform or change the implementation of later ones, we will work one feature at a time from planning through implementation, completion, and human validation, before moving on to the next.

The following guidelines MUST always be followed:

* Features that are non-trivial in size (i.e. more than a few simple changes) should be broken down into Milestones and Tasks. Those will be given a prefix to be used in commit messages, formatted as `{Feature Name} - {Milestone number}.{Task number}`. Human approval must always be obtained to move from one Milestone to the next.
* Before beginning a feature, you must be on a git branch other than `main`. If you are not, start a new branch named after the feature.
* The first task of every feature must be writing your complete implementation plan to the original feature markdown document.
* At the end of every Milestone and Feature you must (in order):
  1. Update the feature markdown document to indicate what progress has been made on the relevant Milestone or Feature.
  2. Commit that along with all changes to git, using a commit message beginning with the Milestone/Task prefix and a one-sentence concise summary of the changes followed by a detailed explanation of the changes.
  3. Build the rendered blog, start the server in the background, and request human confirmation that the results appear as expected visually.
  4. Open a GitHub PR to merge the feature branch to `main`.
* Every feature must end with an "Acceptance Criteria" Milestone. This Milestone must include tasks to:
  1. As the last step of every feature, move the feature markdown file from `docs/features/` to `docs/features/completed/`.
* If you become confused or unclear on how to proceed, have to make a significant decision not explicitly included in the implementation plan, or find yourself making changes and then undoing them without a clear and certain path forward, you must stop and ask for human guidance.
* From time to time we may identify a new, more pressing issue while implementing a feature; we refer to these as "side quests". When beginning a side quest you must update this document to include detailed information on exactly where we're departing from our feature implementation, such that we could use this document to resume from where we left off in a new session, and then commit that. When the side quest is complete, we will resume our feature work.
* If we identify a significant body of work that we need to complete but we (be sure to include the human in this decision) feel is outside the scope of the current feature, we MUST write and commit a new feature file for it (using `docs/features/template.md`).

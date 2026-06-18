# Source Notes

These notes summarize the materials used to build this skill. Do not quote long passages; use them to ground recommendations.

## Local Source Files

- Agent instruction file best-practice notes
- AI coding agent project context guidance
- Instruction-file maintenance and pruning notes

## Article Notes

- Agent instruction files should be treated as technical briefs rather than persona prompts.

## Distilled Claims

- `AGENTS.md` is best treated as a tool-neutral README for agents.
- The highest-value content is exact operational context: commands, structure, non-default conventions, testing, safety, and known gotchas.
- Concision matters because these files are loaded into the agent context. Long, irrelevant, or generic instructions reduce adherence.
- Use progressive disclosure: root files should route to deeper docs, nested instruction files, rules, commands, skills, or hooks when needed.
- Keep shared `AGENTS.md` focused on stable project facts and avoid mixing in personal habits.
- Reserve emphasized critical rules for a small number of constraints that prevent specific repeated mistakes.
- Prefer deterministic tools for formatting, linting, type checking, secret scanning, and repeatable validation.
- Mature setups evolve from absent/basic files to scoped, structured, path-aware, maintained, and adaptive systems.
- Security guidance should describe where secrets live and how to access them safely, never include the values.
- Effective files are maintained like code: reviewed, pruned, updated when commands or architecture change, and improved after repeated agent mistakes.
- A useful maintenance loop is to add rules after the agent repeatedly makes a concrete mistake, not to pre-fill a giant rulebook on day one.

## Tensions In The Sources

- Some sources recommend many common sections; others argue for aggressively short files. Resolve this by starting from the common section list, then deleting anything not project-specific, stable, and useful in most sessions.
- Some sources mention generated `/init` files as useful starts; others warn against accepting generated files blindly. Resolve this by using generated output only as a draft to be reviewed line-by-line.
- Advanced features such as skills, hooks, and MCP can be powerful but are not automatically better. Recommend them only when they reduce repeated friction or context noise.

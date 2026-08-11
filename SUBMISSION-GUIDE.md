# Skill Tile Submission Guide

Use the details below to fill in the "Register a New Skill" issue form.

---

## Issue Title

```
Super Business Network Skills — SAP Business Network Catalog & Integration Enablement
```

---

## Repository URL

```
https://github.com/FaheemSAP/super-business-network-skills
```

---

## Skills in this repository

```
super-business-network-skills — SAP Business Network expert for supplier catalog enablement, cXML integration lifecycle, document anonymization, supply chain collaboration, BN4L logistics, and API guidance. Covers 7 domains with advisory + artifact generation.
```

---

## Readiness Checklist

- [x] The repository is public on github.com
- [x] Each skill has a `skills/<slug>/SKILL.md` file with `name` and `description` frontmatter
- [x] Author information is available (in README and package.json)
- [x] License information is available (Apache 2.0 LICENSE file and package.json)

---

## Steps to Upload

1. **Create a new public GitHub repo** named `super-business-network-skills`
2. **Push the contents** of the `super-business-network-skills-repo/` folder to the repo:
   ```bash
   cd super-business-network-skills-repo
   git init
   git add .
   git commit -m "Initial commit: Super Business Network Skills v2.0.0"
   git branch -M main
   git remote add origin https://github.com/your-org/super-business-network-skills.git
   git push -u origin main
   ```
3. **Go to the AI Skills Library** issue tracker and create a new issue using the "Register a New Skill" template
4. **Fill in the fields** using the values above
5. **Submit** — a maintainer will review and add your repo to the library

---

## Repository Structure Verification

```
super-business-network-skills/          ← repo root
├── .gitignore
├── LICENSE                             ← Apache 2.0 ✓
├── README.md                           ← Author info ✓
├── package.json                        ← Metadata ✓
├── SUBMISSION-GUIDE.md                 ← This file (can delete after submission)
└── skills/
    └── super-business-network-skills/  ← skill slug ✓
        ├── SKILL.md                    ← name + description frontmatter ✓
        ├── references/
        │   ├── bn4l-logistics.md
        │   ├── catalog-hub.md
        │   ├── catalog-processing.md
        │   ├── cxml-anonymizer.md
        │   ├── integration-hub.md
        │   ├── sap-apis.md
        │   └── supply-chain-collaboration.md
        ├── scripts/
        │   └── anonymize_cxml.py
        └── assets/
            └── evals.json
```

All checklist requirements are met. Ready to submit.
�� evals.json
```

All checklist requirements are met. Ready to submit.

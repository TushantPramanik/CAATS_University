# What the uploaded project already does

This web version was mapped from the eight uploaded files. The uploaded Python files remain unchanged; the website lives in this separate `web-app` folder.

## Existing flow

1. `A_main(2).py` offers registration, login, and a password recovery prompt, then starts the personal details flow. Its account data only lives in Python variables, so it is lost when the program exits. The recovery prompt accepts a new password without verifying an old one.
2. `B_user_details(2).py` asks whether the visitor is a student, working, or other, then asks for one of six age bands. Students under 13 go to skills; ages 13–17 can choose their age-matched school class or skills; 17+ can choose college or skills. Working visitors must be 17+ and can choose skills or a four-hour master class. Other visitors go to skills.
3. `C_school_dep(2).py` offers Boards or Olympiad for classes 9–12.
4. `D_work_dep(2).py` lists six skill areas and four four-hour master classes.
5. `E_clg_brch_choos(2).py` uses class 12 marks to show college courses: 75–100 gives BTech, BSc, BCA, and Diploma; 55–below 75 gives BSc, BCA, Diploma; 40–below 55 gives BSc and Diploma; 33–below 40 gives Diploma; below 33 says admission is not possible.
6. `F_Btech_clg_dep(2).py` uses CAATS JEE percentile bands and the visitor’s interest to show engineering branches.
7. `G_Bsc_clg_dep(2).py` and `I_Bca_clg_dep.py` show subject/branch options based on class 12 percentage.

## Rules carried into the site

- School age-to-class mapping and Boards/Olympiad choices match `B_user_details(2).py` and `C_school_dep(2).py`.
- Skills and master class options match `D_work_dep(2).py`.
- College course thresholds match `E_clg_brch_choos(2).py`.
- BSc and BCA subject choices follow the percentage bands in their respective uploaded files.
- BTech interest and branch options follow the tables in `F_Btech_clg_dep(2).py`.
- Recommendations are saved with the account in SQLite. Passwords are stored as salted PBKDF2 hashes, not plain text.

## Source questions to decide

These issues are present in the source, so the site reports them instead of quietly inventing a rule:

- **BCA 70% to below 75%:** no `if` branch handles this range. The site records that no recommendation is defined.
- **BSc exactly 40%:** the `>=40 and <45` branch offers Biotechnology, but a later `<=40` branch says not eligible. The website follows the Biotechnology branch at exactly 40% and attaches a warning.
- **BTech decimal percentile:** the code uses whole-number bands such as 75–84 and 65–74, so decimal values between bands are not covered. The site flags decimal scores when a result is produced; uncovered values have no defined branch.
- **Diploma:** the college flow imports `K_diploma_clg_dep.py`, which was not among the eight uploads. The site can save a Diploma selection but does not claim eligibility or course rules.
- **Follow-up actions:** the course and school modules import `L_bat_prch.py`, also not uploaded. The site carries over the destination choices but not the missing follow-up/practice actions.
- **Age labels:** the source age bands overlap at some real ages (for example, 13–14 and 14–15). The site preserves the same labels and does not convert a numeric age into a band.
- **BTech programming at 75–84:** the source shows Programming as an interest but its branch-choice block has no Programming case. The site lists the interest from the source and will return an explicit validation message instead of silently selecting a branch.

This counselling result is a faithful project demo, not an official admission decision. Eligibility depends on the simplified rules in the original console project.

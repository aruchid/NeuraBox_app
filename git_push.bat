@echo off
echo Starting Git operations...

:: Add all changes
git add .
echo Files added successfully.

:: Commit with message "update"
git commit -m "update"
echo Changes committed successfully.

:: Push to remote repository
git push
echo Changes pushed to remote repository.

echo Git operations completed.
pause 
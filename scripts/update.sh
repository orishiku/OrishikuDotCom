#!/bin/sh
cd /home/orishiku/OrishikuDotCom;

git stash;
git fetch --all;
git checkout origin/develop;
git stash pop;

touch src/OrishikuDotCom/wsgi/site.py;
touch src/OrishikuDotCom/wsgi/blog.py;

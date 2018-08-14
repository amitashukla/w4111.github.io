#!/bin/sh
git tag -d joinsubmit
git push origin :refs/tags/joinsubmit
git add --all .
git commit -a -m 'Join lab'
git tag -a lab1submit -m 'submit join lab'
git push origin master --tags

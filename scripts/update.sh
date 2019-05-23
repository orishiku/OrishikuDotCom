#!/bin/bash

while getopts p:b: option
do
case "${option}"
in
	p) ROOT_PATH=${OPTARG};;
	b) BRANCH=${OPTARG};;
esac
done

if [ "$ROOT_PATH" != "" ]; then
	# Enter root path of project
	cd $ROOT_PATH;

	if [ "$BRANCH" != "" ]; then
		echo ""
		echo -e "\e[32m######### Update git project #########";
		echo ""
		echo -e "\e[33m-- $BRANCH --\e[39m"
		echo ""
		git fetch --all;
		git reset --hard origin/$BRANCH
	else
		echo ""
		echo -e "\e[91mERR: -b 'release branch' is needed"
	fi

	echo ""
	echo -e "\e[32m######### Update django project #########";

	# Load python environment
	source ../odc_env/bin/activate;

	# Set sites settings
	SETTING[0]=OrishikuDotCom.settings.site
	SETTING[1]=OrishikuDotCom.settings.blog

	# Run django commands for each site
	for s in ${SETTING[@]}; do
		echo ""
		echo -e "\e[33m-- $s --\e[39m";
		python src/manage.py collectstatic --settings=$s --noinput;
		python src/manage.py migrate --settings=$s;
	done

	# Restart wsgi servers
	echo ""
	echo -e "\e[33m-- Reload wsgi server --\e[39m";
	
	# delay to give webhook oportunity to get an answer from django
	echo ""
	echo -e -n "\e[5mwait..."
	sleep 5;
	
	touch src/OrishikuDotCom/wsgi/site;
	touch src/OrishikuDotCom/wsgi/blog;
	echo -e "\r\e[0mdone   "
	echo ""
else
	echo ""
	echo -e "\e[91mERR: -p 'project root_path' is needed"
fi
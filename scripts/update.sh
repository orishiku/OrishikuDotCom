#!/bin/bash
#ssh -C orishiku@134.209.8.96 ~/dumpDB.sh; scp -r orishiku@134.209.8.96:~/dumpdb.json /home/orishiku/Workspace/Web/OrishikuDotCom/;python src/manage.py loaddata dumpdb.json --settings=OrishikuDotCom.settings.blogDev
#./update.sh -p /home/orishiku/OrishikuDotCom/  -b release/alpha_1.0

#https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password
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
	service apache2 restart;
	echo -e "\r\e[0mdone   "
	echo ""
else
	echo ""
	echo -e "\e[91mERR: -p 'project root_path' is needed"
fi
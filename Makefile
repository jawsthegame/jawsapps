update_requirements:
	cat ./jawsapps_req.txt \
		./explorify-server/requirements.txt \
		./bikerite/server/requirements.txt \
	| sort \
	| uniq \
	> requirements.txt

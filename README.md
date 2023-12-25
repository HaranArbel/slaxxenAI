# API Backend 

The apis avalible to query:

## Get dashboard statistics
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/general_stats/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'<br />
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/financial_stats/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'<br />
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/social_stats/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'<br />
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/fundraising_stats/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'<br />
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/geo_stats/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'<br />

## Get Identity
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/get_identity/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8'

## Load Identity
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/upload_identity/' --header 'Content-Type: application/json' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8' \
--data '{"name": "Test Abu Test 2", "id": "AA2232588888", "dob": "11/01/1968", "israel_designation_date": "01/01/2022", "nationality_residency": "Barbados", "designated_by": "Israel", "foreign_designation_date": "test", "designation_id": "test", "update_date": "2023-12-06 16:59:06.267115"}'

## Load File
curl --location 'https://sbaas-ap3gm5u7tq-uc.a.run.app/upload_file/' --header 'SBaaS-API-Key: ab96e0fb-1cff-49b7-98b9-8737a8a797d8' --form 'file=@"/Users/AAA/Downloads/NBCTF_Individuals.csv"'


## [Link to ERD](https://dbdiagram.io/d/65806a9f56d8064ca03fc746)

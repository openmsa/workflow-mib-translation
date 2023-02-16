# MIB Translation Workflow
Assurance MIB Translation Workflow

The goal of this workflow is to implement translation rules of an OID into a string from Management Information Base (MIB)

The workflow installation or update have to be done in the **msa-dev** container, for that the following command can help
```
docker exec -it $(docker ps -q -f name=msa-dev) bash
```

## How to install this workflow in the MSA
In the **msa-dev** container
```
cd /opt/fmc_repository/
git clone https://github.com/openmsa/workflow-mib-translation.git
chown -R ncuser. workflow-mib-translation
cd Process
ln -s ../workflow-mib-translation/ .
chown -R ncuser. workflow-mib-translation
```

Once done, **workflow-mib-translation** is available in the list of workflows in the MSA UI

## How to update this workflow in the MSA
In the **msa-dev** container
```
cd /opt/fmc_repository/workflow-mib-translation
git fetch -p
git status
```
Fix conflict if any and then
```
git pull
chown -R ncuser. .
```

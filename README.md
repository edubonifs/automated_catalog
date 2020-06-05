# AUTOMATED CATALOG

This project is created due to the necessity of saving some time for the consultants at the time of being in a delivery. It is though to provide consultants a testing environment as soon as possible so that some tests can be made withouth risking by doing them in a productive environment.

Currently, the program is able to automatically install Satellite, Tower, IDM and OCP 3.11 prerequisites.

## Getting Started

This project was developed initially in quicklab, although it has been made to be used in any platform.

For starting you may clone the project: git clone https://github.com/edubonifs/automated_catalog.git

### Prerequisites

Before starting, you may have your node subscribed with a valid redhat subscription, and have python and ansible 2.8 installed.

subscription-manager repos --enable ansible-2.8-for-rhel-8-x86_64-rpms

yum install ansible

## Running the program

For running the program you just have to run the automated.py file:

python automated.py

You will be prompted with some questions, in which you will just have to enter numbers (1,2,3...) or strings, normally for hostnames, users or passwords.

## Authors

Eduardo Bonilla Rodríguez

Junior Consultant Red Hat


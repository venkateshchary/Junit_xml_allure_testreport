# Junit_xml_allure_testreport
Creating the junit xml files using the python junitparser . and generate the test report using the allure 

## Some links for more in depth learning and installation
### installation in windows
* [scoop installation in windows](https://www.onmsft.com/how-to/how-to-install-the-scoop-package-manager-in-windows-10) A website for instalation process description.
* [JDK installation](https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html) A website for instalation of JDK.
* [JAVA_HOME setup](https://stackoverflow.com/questions/2619584/how-to-set-java-home-on-windows-7/17142065#17142065) Information to set up Java_home in environmental setup.

The Powershell Flow commands
==================
- Set-ExecutionPolicy RemoteSigned -scope CurrentUser
- iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
- scoop install allure
- allure --version
- allure serve </Folder path of xml files>

Creating Junit xml test suite files
------------
Using the python packages we can create the xml files
- Pip install below packages
    - pip install junitparser {{https://pypi.org/project/junitparser/}}
    - pip install junit-xml   {{https://pypi.org/project/junit-xml/}}
    

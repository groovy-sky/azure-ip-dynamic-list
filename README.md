# Get Azure IP ranges using Python function

## Introduction

This document gives an example how you can use Azure function to obtain and display Azure IP ranges. This function can be used in PAN-OS as URL for 'External Dynamic List'. 

## Theoretical Part

Azure Functions allows you to run small pieces of code (called "functions") without worrying about application infrastructure. With Azure Functions, the cloud infrastructure provides all the up-to-date servers you need to keep your application running at scale.

A function is "triggered" by a specific type of event. Supported triggers include responding to changes in data, responding to messages, running on a schedule, or as the result of an HTTP request.

Azure Functions has three kinds of pricing plans:

* **Consumption plan**: Azure provides all of the necessary computational resources. You don't have to worry about resource management, and only pay for the time that your code runs.

* **Premium plan**: You specify a number of pre-warmed instances that are always online and ready to immediately respond. When your function runs, Azure provides any additional computational resources that are needed. You pay for the pre-warmed instances running continuously and any additional instances you use as Azure scales your app in and out.

* **App Service plan**: Run your functions just like your web apps. If you use App Service for your other applications, your functions can run on the same plan at no additional cost.

In PAN-OS an External Dynamic List is a text file that is hosted on an external web server so that the firewall can import objects—IP addresses, URLs, domains—included in the list and enforce policy. To enforce policy on the entries included in the external dynamic list, you must reference the list in a supported policy rule or profile. As you modify the list, the firewall dynamically imports the list at the configured interval and enforces policy without the need to make a configuration change or a commit on the firewall. 

## Practical Part

### ARM template deployment

Everything you need for a deployment is located in this repository. At first you need to deploy ARM template, located under '/Template/azuredeploy.json' path. To do so you can use any preferable option you want or just click on the button below:

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgroovy-sky%2Fazure-ip-dynamic-list%2Fmaster%2FTemplate%2Fazuredeploy.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.png"/>
</a>

As a result will be deployed a function, storage account and consumption app service plan:
![](/Images/azure_resources.png)

### Function publish

To publish the function's code, please follow the instruction:

1. Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and [Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#v2)
2. Clone this repository locally
3. Go to 'Function' folder and run following command(where `<FunctionAppName>` should be your function name):
`func azure functionapp publish <FunctionAppName> --python`

Deployment should take less than 5 minutes:
![](/Images/azure_deploy.gif)

More information about a deployment options you can find [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#project-file-deployment).

## Results

As soon as application was published you will get an unique URL. By accessing it you should get current available regions list. At the time of writing available regions are:
`['australiac2', 'australiac', 'australiaeast', 'australiasoutheast', 'brazilsouth', 'brazilse', 'canadacentral', 'canadaeast', 'indiacentral', 'uscentraleuap', 'uscentral', 'asiaeast', 'useast2euap', 'useast2', 'useast', 'francec', 'frances', 'germanyn', 'germanywc', 'japaneast', 'japanwest', 'koreacentral', 'koreasouth', 'usnorth', 'europenorth', 'norwaye', 'norwayw', 'southafrican', 'southafricaw', 'ussouth', 'indiasouth', 'asiasoutheast', 'switzerlandn', 'switzerlandw', 'uaec', 'uaen', 'uknorth', 'uksouth2', 'uksouth', 'ukwest', 'uswestcentral', 'europewest', 'indiawest', 'uswest2', 'uswest']`

Now, for example, if you want to get IP list from West Europe - just append URL with `&location=europewest` and check the result:
![](/Images/palo_func.png)


## Related links

* https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClVYCA0

* https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#project-file-deployment

* https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/minemeld

* https://azuredcip.azurewebsites.net/getazuredcipranges

* https://buildwindows.wordpress.com/2017/11/19/get-azure-datacenter-ip-ranges-via-api/

* https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function
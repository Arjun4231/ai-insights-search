# OPEN AI API based Documents query start kit

## Introduction
### This is just a starter kit and not for production. A lot needed for production like Dev Ops based attributes etc etc 
### This code leverages Langchain APIs for Open AI
### This ai application reads the PDF documents kept in "docs" folder and allows you to query based on the documents. 
### You can change Title / Documents as per your requirements. It is a flexible application although current implementation is done for "enquiring" of airport lounges based on the two documents inside "./docs" folder.  

## Pre-requisits 
### Install Docker on your machine 

## Customization 
### Update below attributes inside "./config.py"
### Mandatory is openapi_key which you need to buy :) from https://platform.openai.com/account/api-keys 

## Installations & Run

### clone this repo
### docker build -t doc-query-starter .
### docker run -p 8080:8080 doc-query-starter
### Go to localhost:8080. Sample query without "Customization" is `list all lounges in New Delhi`
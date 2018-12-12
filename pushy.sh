#!/bin/bash

git push
curl -X POST http://grizzlyauto:115b885396b8580b803d8e4e59df2148e3@jenkins.mtop.local:8080/job/CPM-RestAPI-Lib/build?token=ce9e15551dcef8f03d22b9f331b0417f 

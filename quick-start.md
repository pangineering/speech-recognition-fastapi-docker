---
description: How to install
---

# Installation

## List of Libraries in the requirement.txt

```
anyio==3.6.1
certifi==2022.6.15
charset-normalizer==2.1.0
click==8.1.3
cycler==0.11.0
fastapi==0.78.0
filelock==3.7.1
fonttools==4.33.3
h11==0.13.0
httptools==0.4.0
huggingface-hub==0.8.1
idna==3.3
kiwisolver==1.4.3
matplotlib==3.5.2
numpy==1.23.0
packaging==21.3
Pillow==9.2.0
pydantic==1.9.1
pyparsing==3.0.9
python-dateutil==2.8.2
python-dotenv==0.20.0
python-multipart==0.0.5
PyYAML==6.0
regex==2022.6.2
requests==2.28.1
six==1.16.0
sniffio==1.2.0
SpeechRecognition==3.8.1
starlette==0.19.1
tokenizers==0.12.1
torch==1.12.0
torchaudio==0.12.0
torchvision==0.13.0
tqdm==4.64.0
transformers==4.20.1
typing_extensions==4.3.0
urllib3==1.26.9
uvicorn==0.18.2
uvloop==0.16.0
watchfiles==0.15.0
websockets==10.3
```

## Install the library

{% tabs %}
{% tab title="Python" %}
```
# Install via pip
pip install -r requirement.txt
```
{% endtab %}
{% endtabs %}

## Make your first request

To make your first request, send an authenticated request to the pets endpoint. This will create a `pet`, which is nice.

{% swagger baseUrl="https://api.myapi.com/v1" method="post" path="/pet" summary="Create pet." %}
{% swagger-description %}
Creates a new pet.
{% endswagger-description %}

{% swagger-parameter in="body" name="name" required="true" type="string" %}
The name of the pet
{% endswagger-parameter %}

{% swagger-parameter in="body" name="owner_id" required="false" type="string" %}
The 

`id`

 of the user who owns the pet
{% endswagger-parameter %}

{% swagger-parameter in="body" name="species" required="false" type="string" %}
The species of the pet
{% endswagger-parameter %}

{% swagger-parameter in="body" name="breed" required="false" type="string" %}
The breed of the pet
{% endswagger-parameter %}

{% swagger-response status="200" description="Pet successfully created" %}
```javascript
{
    "name"="Wilson",
    "owner": {
        "id": "sha7891bikojbkreuy",
        "name": "Samuel Passet",
    "species": "Dog",}
    "breed": "Golden Retriever",
}
```
{% endswagger-response %}

{% swagger-response status="401" description="Permission denied" %}

{% endswagger-response %}
{% endswagger %}

{% hint style="info" %}
**Good to know:** You can use the API Method block to fully document an API method. You can also sync your API blocks with an OpenAPI file or URL to auto-populate them.
{% endhint %}

Take a look at how you might call this method using our official libraries, or via `curl`:

{% tabs %}
{% tab title="curl" %}
```
curl https://api.myapi.com/v1/pet  
    -u YOUR_API_KEY:  
    -d name='Wilson'  
    -d species='dog'  
    -d owner_id='sha7891bikojbkreuy'  
```
{% endtab %}

{% tab title="Node" %}
```javascript
// require the myapi module and set it up with your API key
const myapi = require('myapi')(YOUR_API_KEY);

const newPet = away myapi.pet.create({
    name: 'Wilson',
    owner_id: 'sha7891bikojbkreuy',
    species: 'Dog',
    breed: 'Golden Retriever',
})
```
{% endtab %}

{% tab title="Python" %}
```python
// Set your API key before making the request
myapi.api_key = YOUR_API_KEY

myapi.Pet.create(
    name='Wilson',
    owner_id='sha7891bikojbkreuy',
    species='Dog',
    breed='Golden Retriever',
)
```
{% endtab %}
{% endtabs %}

<h1>SETUP & INSTALLATION </h1>
1. Build Image

```
make build
```

2. Create Network

```
make init_network
```

3. Start DB container

```
make db
```

4. Start App container

```
make app
```

5. Stop DB & App

```
make stop
```

---

<h1> API DOCUMENTATION</h1>

<ul><li>Users</li></ul>

<p>Get Users</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/users
```

<p>Get User By Id</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/users/5f468aa4432c142b7e3bf6f1
```

<p>Create User</p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1/users \
  --header 'Content-Type: application/json' \
  --data '{
	"name" : "Michael Jay",
	"phone" : "3841",
	"age" : 19
}'
```

---

<ul><li>Medicine</li></ul>
<p>Get Medicine</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/medicines
```

<p>Get Medicine By Id</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/medicines/5f46b7a6a2b9b61d4647b270

```

<p>Create Medicine</p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1/medicines \
  --header 'Content-Type: application/json' \
  --data '{
	"name" : "Zinc",
	"group_name" : "Mineral",
	"med_type" : 0
}'

```

---

<ul><li>Dosage</li></ul>

<p>Get Dosages</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/dosages
```

<p>Get Dosage By Id</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/dosages/5f483211554108ecaaeef835
```

<p>Create Dosage</p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1/dosages \
  --header 'Content-Type: application/json' \
  --data '{
	"medicine" : "5f4842096e0bb4574f6b6a2b",
	"amount_bought" : 50,
	"frequency" : 2,
	"quantity" : 2
}'
```

<p>Create Medicine & Dosage</p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1.1/dosages \
  --header 'Content-Type: application/json' \
  --data '{
	"medicine": {
		"name": "Tusca",
		"group_name": "ChronBron",
		"med_type": 1
	},
	"amount_bought": 150,
	"frequency": 3,
	"quantity": 15
}'
```

<ul><li>Prescription</li></ul>

<p> Get Prescriptions</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/prescriptions
```

<p> Get Prescription By Id</p>

```
curl --request GET \
  --url http://127.30.1.1:6161/api/v1/prescriptions/5f483d037b00849f4ea065c6
```

<p>Create Prescription</p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1/prescriptions \
  --header 'Content-Type: application/json' \
  --data '{
	"user" : "5f4841da6e0bb4574f6b6a2a",
	"dosage" : "5f48438c7556a239f4fc9f54"
}'
```

<p> Create Medicine, Dosage, Prescription </p>

```
curl --request POST \
  --url http://127.30.1.1:6161/api/v1.1/prescriptions/ \
  --header 'Content-Type: application/json' \
  --data '{
	"user": "5f4841da6e0bb4574f6b6a2a",
	"medicine": {
		"name": "CalciumSSD",
		"group_name": "VitaminD",
		"med_type": 0
	},
	"amount_bought": 20,
	"frequency": 1,
	"quantity": 2
}'
```

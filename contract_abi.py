abi = """[
	{
		"constant": true,
		"inputs": [],
		"name": "getCurrentOpinion",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_soapboxer",
				"type": "address"
			}
		],
		"name": "isApproved",
		"outputs": [
			{
				"name": "approved",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_opinion",
				"type": "string"
			}
		],
		"name": "broadcastOpinion",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"payable": true,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_soapboxer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_opinion",
				"type": "string"
			}
		],
		"name": "OpinionBroadcast",
		"type": "event"
	}
]"""
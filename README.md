Check it out [here](https://banks-rest-api.herokuapp.com/)

# Endpoints

- GET `/branches/:IFSC` - gets the branch with specific ifsc code.
	
	_example request_: `/branches/JAKA0AZGUNJ`
	_returns_ a single object with following signature:
	```
	{
		"url": String,
		"bank": String,
		"branch": String,
		"address": String,
		"city": String,
		"district": String,
		"state": String
	}
	```
	_note: enter IFSC code in capital letters only_

- GET `/branches` - gets the list of all branches, page-wise

	_returns_ list with following signature:
	```
	{
		"count": Number,
		"next": String,
		"previous": String,
		"results": List<branch>
	}
	```
	**query params**
	- `city` - branches in that city

		_example_: `/branches?city=delhi`
	
	**bank_name** - branches of that specific bank
	
		example: `/branches?bank_name=jammu+and kashmir+bank+limited`
			
	*These two can also be combined*
	
	_example_: `/branches?city=delhi&bank_name=jammu+and kashmir+bank+limited`
	will get list of branches of `bank_name` in that `city`

	note:
	- _pages can be accessed via `?page=n` query_
	- _`next` and `previous` fields are links to next and previous pages respectively_

# Source

data dump from https://github.com/snarayanank2/indian_banks
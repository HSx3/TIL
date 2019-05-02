const axios = require('axios');
url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts/'

// get
axios.get(url)
    .then(res => {
        console.log(res.data.posts)
    })

// post
const data = {
	"post": {
		"title": "Sample get request",
		"content": "Send this request via XMLHTTPRequest",
		"author": "Master Tester",
	}
}
axios.post(url, data)
    // .then(() => console.log(''))
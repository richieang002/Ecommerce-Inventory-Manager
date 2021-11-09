import axios from 'axios'

axios.defaults.baseURL = "http://localhost:8000/";

if(localStorage.getItem('token'))
    axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');

export default axios
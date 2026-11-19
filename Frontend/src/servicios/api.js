import axios from 'axios';

function getCookie(name){
    const value = `; ${document.cookie}`
    const part = value.split(`; ${name}=`)
    if (part.length === 2) {
        return part.pop().split(";").shift();
    }
    return null
}   

export const api = axios.create({
    baseURL: 'http://localhost:8000/api',
    withCredentials: true,
    headers: {
        "Content-Type": 'application/json'
    }
})

api.interceptors.request.use(
    (config) => {
        const method = config.method?.toLowerCase();
        const unsafeMethods = ["post","put","delete","patch",]
    
        if (method && unsafeMethods.includes(method)){
            const csrfcookie = getCookie('csrftoken')
                if (csrfcookie){
                    config.headers["X-CSRFToken"] = csrfcookie
                }
            
        }
        return config;
    },
    (error) => Promise.reject(error)
)
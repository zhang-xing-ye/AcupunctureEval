import axios from 'axios'
import qs from 'qs'

const baseURL = window.location.protocol + '//' + window.location.hostname + ':8000'

const service = axios.create({
    baseURL,
    headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
    // 主要用于序列化params（params 参数用在get请求上）
    paramsSerializer: params => {
        if (params) {
            //qs.stringify 的{arrayFormat: 'repeat'} 可以对数组转换格式处理成 ids=1&ids=2
            return qs.stringify(params, { arrayFormat: 'repeat' });
        }
    },
    /* 设置请求超时时间*/
    timeout: 30000, // request timeout
    // `transformRequest` 允许在向服务器发送前，修改请求数据
    // 只能用在 'PUT', 'POST' 和 'PATCH' 这几个请求方法
    transformRequest: (data, headers) => {
        if (headers['Content-Type']) {
            if ((headers['Content-Type']).indexOf('multipart/form-data') > -1) { // 上传文件处理
                headers['Content-Type'] = ""
                const formData = new FormData()
                for (let key in data) {
                    formData.append(key, data[key])
                }
                return formData
            } else if ((headers['Content-Type']).indexOf('application/json') > -1) { // 请求json数据格式处理
                return JSON.stringify(data)
            } else { // 其他都是按照 x-www-form-urlencoded数据格式处理
                //qs.stringify 的{arrayFormat: 'repeat'} 可以对数组转换格式处理成 ids=1&ids=2
                return qs.stringify(data, { arrayFormat: 'repeat' })
            }
        } else { // headers['Content-Type'] 不存在时，按照 x-www-form-urlencoded 数据格式处理
            //qs.stringify 的{arrayFormat: 'repeat'} 可以对数组转换格式处理成 ids=1&ids=2
            return qs.stringify(data, { arrayFormat: 'repeat' })
        }
    }
})

// response 拦截器
service.interceptors.response.use(
    response => {
        return response.data
    },
    error => {
        console.log('err' + error) // for debug
        return Promise.reject(error);
    }
)

export default service
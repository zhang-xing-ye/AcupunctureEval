import request from '@/utils/request'

export const getQALeaderboard = (params) => {
    return request({
        url: '/qa/data',
        method: 'get',
        params
    })
}

export const qaEvaluate = (data) => {
    return request({
        url: '/qa/evaluate',
        method: 'post',
        data,
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
}
import axios from 'axios'

const baseURL = '/api/users'

const getAll = async () => {
    try {
        return await axios.get(baseURL)
    } catch (e) {
        console.log("Error retrieving Users")
        throw e
    }
}

export const UserService = {
    getAll,
}
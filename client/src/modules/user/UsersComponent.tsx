import { useState, useEffect } from "react"
import UserType from "./UserType"
import { UserService } from "./UserService"
import UserComponent from "./UserComponent"

const UsersComponent = () => {

    const [users, setUsers] = useState<UserType[]>([])

    useEffect(() => {
        const fetchUsers = async () => {
            const res = await UserService.getAll()
            
            if(res.data.length == 0) setUsers([])
            else setUsers(res.data)
        }

        fetchUsers()
    }, [])

    const usersDisplay = users.length == 0 ? <p>No users available</p> : users.map((u) => <UserComponent key={u.id} user={u} />)

    return (
        <div>
            {usersDisplay}
        </div>
    )
}

export default UsersComponent
import UserType from "./UserType"

interface PropTypes {
    user: UserType
}

const UserComponent = ({user}: PropTypes) => {
    return (
        <div className="mb-2">
            <p>{user.username}</p>
            <p>{user.email}</p>
        </div>
    )
}

export default UserComponent
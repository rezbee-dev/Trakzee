interface PropTypes {
    username: string;
}

const UserHomePage = ({username}: PropTypes) => {
    return (
        <h1>{username}</h1>
    )
}

export default UserHomePage
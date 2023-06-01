import UsersComponent from "./modules/user/UsersComponent"

function App() {

  return (
    <div className="h-screen flex flex-col justify-center items-center">
      <h1 className="text-3xl font-bold underline mb-4">Users!</h1>
      <UsersComponent />
    </div>
  )
}

export default App

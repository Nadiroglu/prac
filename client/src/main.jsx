import { ReactDOM } from 'react'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import router from '../routes.jsx'


const router = createBrowserRouter(router)

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<RouterProvider router={router} />)
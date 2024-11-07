import App from "./src/App"
import Home from "./src/components/Home";

const routes = [
    {
        path: '/',
        element: <App />,
        children: [
            {
                path: '/',
                element: <Home />
            }
        ]
    }
]

export default routes;
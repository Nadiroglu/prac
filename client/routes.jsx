import App from "./src/App"
import Home from "./src/components/Home";

const routes = [
    {
        path: '/',
        element: <App />,
        children: [
            {
                index: true,
                element: <Home />
            }
        ]
    }
]

export default routes;
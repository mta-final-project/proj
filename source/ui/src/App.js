import { createBrowserRouter, RouterProvider } from "react-router-dom";
import AppBar from "./layout/AppBar";

const router = createBrowserRouter([
  {
    path: "/",
    element: <h1>ACADEM-EASE</h1>,
  },
]);

function App() {
  return (
    <div className="App">
      <AppBar />
      <RouterProvider router={router} />
    </div>
  );
}

export default App;

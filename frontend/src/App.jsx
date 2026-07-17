import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

function ProtectedRoute({ children }) {

    const token = localStorage.getItem("token");

    if (!token) {

        return <Navigate to="/login" />;

    }

    return children;

}

export default function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route

                    path="/"

                    element={

                        <ProtectedRoute>

                            <Home />

                        </ProtectedRoute>

                    }

                />

                <Route

                    path="/login"

                    element={<Login />}

                />

                <Route

                    path="/register"

                    element={<Register />}

                />

            </Routes>

        </BrowserRouter>

    );

}
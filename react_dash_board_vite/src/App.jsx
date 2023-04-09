import { useState } from "react";
import "./App.css";

import BarChart from "./components/BarChart";
import LineChart from "./components/LineChart";
import { UserData } from "./Data";

function App() {
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [
      {
        label: "User Gained",
        data: UserData.map((data) => data.userGain),
      },
    ],
  });

  return (
    <>
      <BarChart chartData={userData} />
      <LineChart chartData={userData} />
    </>
  );
}

export default App;

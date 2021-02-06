import './App.css';
import SignIn from './components/SignIn';
import Example from './components/Example';

function App() {
  return (
    <div className='App'>
      <SignIn />
      {/*Add components here (sign in component, Google Maps component, etc)*/}
      <Example />
    </div>
  );
}

export default App;

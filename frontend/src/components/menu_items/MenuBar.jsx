import React from 'react';
import '../../styles.scss'

function MenuBarCustom({ logoutFunction }) {
    return (
        <nav className="menu-bar">
            <ul className="menu-items">
                <li className="menu-item">
                    <a href="/user-info">Home</a>
                </li>
                <li className="menu-item logout">
                    <button onClick={logoutFunction}>Logout</button>
                </li>
            </ul>
      </nav>
    );
}
export default MenuBarCustom;
import React from 'react';
import '../../styles.scss'
import Home from '../button/home';

function MenuBarCustom({ logoutFunction }) {

    return (
        <div className="header">
            <div className='header_left'>
                <h2>App Name</h2>
            </div>
            <div className='header_center'>
                <Home />
            </div>
            <div className='header_right'>
                <button>Logout</button>
            </div>
        </div>
    );
}
export default MenuBarCustom;
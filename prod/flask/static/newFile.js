document.addEventListener('DOMContentLoaded', function () {
    const client = new PasswordlessClient({
        apiKey: 'myapplication:public:4364b1a49a404b38b843fe3697b803c8'
    });

    // Autofill signin
    document.getElementById('signinAutofill').addEventListener('click', async function () {
        try {
            const { token, error } = await client.signinWithAutofill();
            if (error) throw error;
            await verifyToken(token);
        } catch (error) {
            console.error('Autofill signin error:', error);
        }
    });

    // Discoverable credentials signin
    document.getElementById('signinDiscoverable').addEventListener('click', async function () {
        try {
            const { token, error } = await client.signinWithDiscoverable();
            if (error) throw error;
            await verifyToken(token);
        } catch (error) {
            console.error('Discoverable signin error:', error);
        }
    });

    // Alias
    document.getElementById('signinWithAlias').addEventListener('click', async function () {
        const alias = document.getElementById('aliasInput').value; // Get user input
        try {
            const { token, error } = await client.signinWithAlias(alias);
            if (error) throw error;
            await verifyToken(token);
        } catch (error) {
            console.error('Alias signin error:', error);
        }
    });

    document.getElementById('signinWithId').addEventListener('click', async function () {
        const userId = document.getElementById('userIdInput').value; // Get user input
        try {
            const { token, error } = await client.signinWithId(userId);
            if (error) throw error;
            await verifyToken(token);
        } catch (error) {
            console.error('User ID signin error:', error);
        }
    });



    async function verifyToken(token) {
        const backendUrl = 'https://localhost:8002'; // Your backend URL
        try {
            const response = await fetch(`${backendUrl}/verify-signin?token=${token}`);
            const verifiedUser = await response.json();
            if (verifiedUser.success) {
                console.log('Signin successful:', verifiedUser.userId);
                // Proceed with user session or redirect
            } else {
                console.error('Failed to verify user:', verifiedUser.error);
            }
        } catch (error) {
            console.error('Network or server error:', error);
        }
    }


    if (Passwordless.isBrowserSupported()) {
        // Enable signin options
    } else {
        console.error('Browser does not support WebAuthn');
    }
});

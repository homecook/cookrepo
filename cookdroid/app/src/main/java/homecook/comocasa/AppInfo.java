package homecook.comocasa;

import android.app.Application;
import android.content.SharedPreferences;
import android.util.Log;
import android.widget.Toast;

/**
 * Maintains the state of the application
 */
public class AppInfo extends Application
{
    private static final String TAG = "AppInfo";

    //Store the userName for application-wide use
    private String userName = "";
    private Integer userId = -1;
    private String password = "";
    private Boolean isLoggedIn = false;

    //Save username and password for easy access
    private static final String PREFS = "prefs";
    private static final String PREF_USERNAME = "username";
    private static final String PREF_USERID = "userid";
    private static final String PREF_EMAIL = "email";
    private static final String PREF_PASSWORD = "password";
    private static final String PREF_AUTOLOGIN = "autologin";
    private SharedPreferences mSharedPreferences;

    // The homecook REST web api instance that is used throughout the application
    public HomecookRESTApiClient homecookRestApi;

    public AppInfo()
    {
        homecookRestApi = new HomecookRESTApiClient();
    }

    //Initializing app instance (set userid, etc) from shared preferences file
    //TODO: Must update this to make sure all information can is validated against the server
    public boolean Initialize()
    {

        // Read the user's name,
        // or an empty string if nothing found
        String userId = mSharedPreferences.getString(PREF_USERNAME, "");

        if (userId == "") {
            // Not logged in...time to go do this
            Toast.makeText(this, "Not logged in, time to login pal...", Toast.LENGTH_LONG).show();
            isLoggedIn = false;
            return false;
        }
        else
        {
            // If the name is valid. OK!
            Toast.makeText(this, "Welcome back " + userId.toString(), Toast.LENGTH_LONG).show();
            this.userName = userId;
            isLoggedIn = true;
            return true;
        }
    }

    //Initializing app instance (set userid, etc) from login page
    public void Initialize(String email, Integer id, String username, String password, boolean saveInfo)
    {
        mSharedPreferences = getSharedPreferences(PREFS, MODE_PRIVATE);

        // Get and set userName
        this.userId = id;
        this.userName = username;
        this.password = password;

        if (saveInfo)
        {
            SharedPreferences.Editor e = mSharedPreferences.edit();
            e.putString(PREF_EMAIL, email);
            e.putString(PREF_PASSWORD, password);
            e.putBoolean(PREF_AUTOLOGIN, true);
            e.putString(PREF_USERNAME, username);
            e.putInt(PREF_USERID, id);
        }

        //TODO: Authenticate homecookRestApi by providing username/password
        homecookRestApi.set_auth(userName, this.password);
        Log.i(TAG, "Successfully initialized app-info, and logged in " + username);

        isLoggedIn = true;

    }

    public void logOut()
    {
        if (isLoggedIn()) {
            // Reset all variables related to user
            userName = "";
            password = "";

            SharedPreferences.Editor e = mSharedPreferences.edit();
            e.putString(PREF_EMAIL, "");
            e.putString(PREF_PASSWORD, "");
            e.putBoolean(PREF_AUTOLOGIN, false);
            e.putString(PREF_USERNAME, "");
            e.putInt(PREF_USERID, -1);
            isLoggedIn = false;
        }

    }

    //TODO: convert this to isLogged in property with get/set
    public boolean isLoggedIn() {
        return isLoggedIn;
    }

    public String getUserName(){
        return userName;
    }

    public Integer getUserId(){
        return userId;
    }

}
package homecook.comocasa;

/**
 * Created by krishan on 16-03-11.
 */

import com.loopj.android.http.*;

public class HomecookRESTApiClient {

    private static final String BASE_URL = "http://10.0.2.2:8000/";    //TODO: modify with the new server
    private AsyncHttpClient client = new AsyncHttpClient();
    private SyncHttpClient sync_client = new SyncHttpClient();

    public void set_auth(String username, String pass){
        client.setBasicAuth(username,pass);
        sync_client.setBasicAuth(username,pass);
    }

    public void get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        client.get(getAbsoluteUrl(url), params, responseHandler);
    }

    public void post(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        client.post(getAbsoluteUrl(url), params, responseHandler);
    }

    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

    /*
    Synchronous http client
     */
    public void sync_get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        sync_client.get(getAbsoluteUrl(url), params, responseHandler);
    }
}
using UnityEngine;

public class BallController : MonoBehaviour
{
    private GameObject owner;
    private Rigidbody rb;
    public float kickForce = 10f;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    public void PassTo(GameObject newOwner)
    {
  
        owner = newOwner;
    }

    public void Kick(Vector3 direction)
    {

        rb.velocity = direction.normalized * kickForce;
    }

    private void OnCollisionEnter(Collision collision)
    {

        if (collision.gameObject.CompareTag("Wall"))
        {

            Vector3 newVelocity = Vector3.Reflect(rb.velocity, collision.contacts[0].normal);
            rb.velocity = newVelocity;
        }
        else if (collision.gameObject.CompareTag("Agent"))
        {
            
        }
    }

}

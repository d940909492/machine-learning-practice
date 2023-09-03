using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;

public class SoccerAgent : Agent
{
    public GameObject ball;
    public float speed = 5f;
    private bool wantsToPass;
    private GameObject teammate;

    public override void Initialize()
    {
        // Initialize the agent, find the ball, and teammate.
        ball = GameObject.FindWithTag("Ball");
        teammate = GameObject.FindWithTag("Teammate");
    }

    public override void OnEpisodeBegin()
    {
        // Reset the environment for a new episode.
        // Reset agent and ball positions.
        // Randomize starting positions if desired.
    }

    public override void CollectObservations(VectorSensor sensor)
    {
        // Observe relevant information such as agent position, ball position, teammate position, etc.
        sensor.AddObservation(transform.position);
        sensor.AddObservation(ball.transform.position);
        sensor.AddObservation(teammate.transform.position);
    }

    public override void OnActionReceived(float[] vectorAction)
    {
        // Determine the action for this step.
        float moveX = vectorAction[0];
        float moveZ = vectorAction[1];
        wantsToPass = vectorAction[2] > 0f;

        // Move the agent based on actions.
        Vector3 moveDirection = new Vector3(moveX, 0f, moveZ).normalized;
        transform.Translate(moveDirection * speed * Time.deltaTime);

        // Handle passing the ball if the agent wants to pass and is close to the teammate.
        if (wantsToPass && Vector3.Distance(transform.position, teammate.transform.position) < 1.0f)
        {
            PassBall();
        }
    }

    private void PassBall()
    {
        // Transfer control of the ball to the teammate.
        ball.GetComponent<BallController>().PassTo(teammate);
    }
}

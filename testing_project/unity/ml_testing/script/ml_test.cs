using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using TMPro;

public class ml_test : Agent
{

    //[SerializeField] private Transform enemy;

    private Rigidbody rb;

    public List<Transform> enemies = new List<Transform>();

    [SerializeField] private float onActSpeed = 6f;

    public float totalReward = 0f;

    private int currentEnemyIndex = 0;

    public spawn_manager spawner;

    public float wallDistance = 1.5f;
    public float enemyDistance = 1f;

    /*
    public void Start()
        {
        Debug.Log("start called");
        rb = GetComponent<Rigidbody>();

        // Add your enemies to the list here or in the Inspector.
        enemies = new List<Transform>();
        foreach (var enemy in GameObject.FindGameObjectsWithTag("enemy"))
        {
            enemies.Add(enemy.transform);
        }
    }
    */

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        // Find all GameObjects with the "enemy" tag and add their Transforms to the list.
        GameObject[] enemyObjects = GameObject.FindGameObjectsWithTag("enemy");
        foreach (var enemyObject in enemyObjects)
        {
            enemies.Add(enemyObject.transform);
        }
    }
    /*
    [SerializeField] private float moveSpeed = 5f;

    private void FixedUpdate()
    {

        float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");

        Vector3 moveDir = new Vector3(moveX, 0f, moveZ).normalized;

        if (moveDir != Vector3.zero)
        {
            Quaternion targetRotation = Quaternion.LookRotation(moveDir);
            transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, Time.fixedDeltaTime * 5f);
        }

        rb.velocity = moveDir * moveSpeed;
    }
*/

    public override void OnEpisodeBegin()
    {
        transform.localPosition = new Vector3(0f, 1.73f, 0f);
        currentEnemyIndex = 0;
        totalReward = 0f;
        DestroyAllEnemies();
    }


    public override void CollectObservations(VectorSensor sensor)
    {
        /*
        //sensor.AddObservation(transform.position);
        Vector3 combinedObservation = new Vector3(transform.position.x, transform.position.y, transform.position.z);
        combinedObservation += enemies[currentEnemyIndex].position;
        sensor.AddObservation(combinedObservation);
        */
        Vector3 combinedObservation = Vector3.zero;

        if (enemies.Count > 0)
        {
            combinedObservation = new Vector3(transform.localPosition.x, transform.localPosition.y, transform.localPosition.z);
            combinedObservation += enemies[currentEnemyIndex].position;
            sensor.AddObservation(combinedObservation);
        }
        else if(enemies.Count <= 0)
        {
            combinedObservation = Vector3.zero;
            sensor.AddObservation(combinedObservation);
        }
    }


    public override void OnActionReceived(ActionBuffers actions)
    {
        float distanceToEnemy = 0;

        if (enemies.Count > 0)
        {
            float moveX = actions.ContinuousActions[0];
            float moveZ = actions.ContinuousActions[1];

            Vector3 moveDirection = new Vector3(moveX, 0, moveZ);

            transform.localPosition += new Vector3(moveX, 0, moveZ) * Time.deltaTime * onActSpeed;

            distanceToEnemy = Vector3.Distance(transform.localPosition, enemies[currentEnemyIndex].localPosition);

            Vector3 toEnemy = enemies[currentEnemyIndex].position - transform.position;
            float Eangle = Vector3.Angle(transform.forward, toEnemy);

            if (distanceToEnemy < 1f)
            {
                AddReward(-0.05f);
                totalReward -= 0.05f;
            }
            else if (Eangle < 90f)
            {
                AddReward(-0.01f);
                totalReward -= 0.01f;
            }
            else if (Physics.Raycast(transform.localPosition, transform.forward, wallDistance, LayerMask.GetMask("wall")))
            {
                AddReward(-0.1f);
                totalReward -= 0.1f;
                EndEpisode();
            }

            
                AddReward(0.1f);
                totalReward += 0.1f;

        }

    }


    public override void Heuristic(in ActionBuffers actionsOut)
    {

        ActionSegment<float> Caction = actionsOut.ContinuousActions;
        Caction[0] = Input.GetAxisRaw("Horizontal");
        Caction[1] = Input.GetAxisRaw("Vertical");
    }


    public void addEnemy()
    {
        currentEnemyIndex++;
    }

    private void OnCollisionEnter(Collision other)
    {
        Debug.Log("touch");

        if (other.gameObject.CompareTag("enemy"))
        {
            AddReward(-10f);
            totalReward -=10f;
            EndEpisode();
            spawner.resetNumber();
        }
        else if (other.gameObject.CompareTag("wall"))
        {
            AddReward(-10f);
            totalReward -= 10f;
            EndEpisode();
            spawner.resetNumber();
        }
    }

    public void DestroyAllEnemies()
    {

        foreach (Transform enemy in enemies)
        {
            if (enemy != null)
            {
                Destroy(enemy.gameObject);
            }
        }
        enemies.Clear();
    }
}
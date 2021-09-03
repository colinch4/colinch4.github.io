---
layout: post
title: "[OpenStack] Commands_ALL"
description: " "
date: 2021-09-03
tags: [OpenStack]
comments: true
share: true
---

### Commands_ALL

>   **acl delete**     Delete ACLs for a secret or container as identified by its href.
>   **acl get**        Retrieve ACLs for a secret or container by providing its href.
>   **acl submit**     Submit ACL on a secret or container as identified by its href.
>   **acl user add**   Add ACL users to a secret or container as identified by its href.
>   **acl user remove**  Remove ACL users from a secret or container as identified by its href.
>   **action definition create**  Create new action.
>   **action definition definition show**  Show action definition.
>   **action definition delete**  Delete action.
>   **action definition list**  List all actions.
>   **action definition show**  Show specific action.
>   action definition update  Update action.
>   action execution delete  Delete action execution.
>   action execution input show  Show Action execution input data.
>   action execution list  List all Action executions.
>   action execution output show  Show Action execution output data.
>   action execution run  Create new Action execution or just run specific action.
>   action execution show  Show specific Action execution.
>   action execution update  Update specific Action execution.
>   address scope create  Create a new Address Scope
>   address scope delete  Delete address scope(s)
>   address scope list  List address scopes
>   address scope set  Set address scope properties
>   address scope show  Display address scope details
>   aggregate add host  Add host to agg regate
>   aggregate create  Create a new aggregate
>   aggregate delete  Delete existing aggregate(s)
>   aggregate list  List all aggregates
>   aggregate remove host  Remove host from aggregate
>   aggregate set  Set aggregate properties
>   aggregate show  Display aggregate details
>   aggregate unset  Unset aggregate properties
>   alarm create   Create an alarm
>   alarm delete   Delete an alarm
>   alarm list     List alarms
>   alarm show     Show an alarm
>   alarm state get  Delete an alarm
>   alarm state set  Delete an alarm
>   alarm update   Update an alarm
>   alarm-history search  Show history for all alarms based on query
>   alarm-history show  Show history for an alarm
>   alarming capabilities list  List capabilities
>   availability zone list  List availability zones and their status
>   baremetal chassis create  Create a new chassis.
>   baremetal chassis delete  Delete a chassis.
>   baremetal chassis list  List the chassis.
>   baremetal chassis set  Set chassis properties.
>   baremetal chassis show  Show chassis details.
>   baremetal chassis unset  Unset chassis properties.
>   baremetal create  Create resources from files (by only specifying the files) or register a new node by specifying one or more optional arguments (DEPRECATED, use 'openstack baremetal node create' instead)
>   baremetal delete  Unregister a baremetal node. DEPRECATED
>   baremetal driver list  List the enabled drivers.
>   baremetal driver passthru call  Call a vendor passthru method for a driver.
>   baremetal driver passthru list  List available vendor passthru methods for a driver.
>   baremetal driver show  Show information about a driver.
>   baremetal introspection abort  Abort running introspection for node.
>   baremetal introspection data save  Save or display raw introspection data.
>   baremetal introspection reprocess  Reprocess stored introspection data
>   baremetal introspection rule delete  Delete an introspection rule.
>   baremetal introspection rule import  Import one or several introspection rules from a json file.
>   baremetal introspection rule list  List all introspection rules.
>   baremetal introspection rule purge  Drop all introspection rules.
>   baremetal introspection rule show  Show an introspection rule.
>   baremetal introspection start  Start the introspection.
>   baremetal introspection status  Get introspection status.
>   baremetal list  List baremetal nodes. DEPRECATED
>   baremetal node abort  Set provision state of baremetal node to 'abort'
>   baremetal node adopt  Set provision state of baremetal node to 'adopt'
>   baremetal node boot device set  Set the boot device for a node
>   baremetal node boot device show  Show the boot device information for a node
>   baremetal node clean  Set provision state of baremetal node to 'clean'
>   baremetal node console disable  Disable console access for a node
>   baremetal node console enable  Enable console access for a node
>   baremetal node console show  Show console information for a node
>   baremetal node create  Register a new node with the baremetal service
>   baremetal node delete  Unregister baremetal node(s)
>   baremetal node deploy  Set provision state of baremetal node to 'deploy'
>   baremetal node inspect  Set provision state of baremetal node to 'inspect'
>   baremetal node list  List baremetal nodes
>   baremetal node maintenance set  Set baremetal node to maintenance mode
>   baremetal node maintenance unset  Unset baremetal node from maintenance mode
>   baremetal node manage  Set provision state of baremetal node to 'manage'
>   baremetal node passthru call  Call a vendor passthu method for a node
>   baremetal node passthru list  List vendor passthru methods for a node
>   baremetal node power  Set power state of baremetal node
>   baremetal node provide  Set provision state of baremetal node to 'provide'
>   baremetal node reboot  Reboot baremetal node
>   baremetal node rebuild  Set provision state of baremetal node to 'rebuild'
>   baremetal node set  Set baremetal properties
>   baremetal node show  Show baremetal node details
>   baremetal node undeploy  Set provision state of baremetal node to 'deleted'
>   baremetal node unset  Unset baremetal properties
>   baremetal node validate  Validate a node's driver interfaces
>   baremetal port create  Create a new port
>   baremetal port delete  Delete port(s).
>   baremetal port list  List baremetal ports.
>   baremetal port set  Set baremetal port properties.
>   baremetal port show  Show baremetal port details.
>   baremetal port unset  Unset baremetal port properties.
>   baremetal set  Set baremetal properties. DEPRECATED
>   baremetal show  Show baremetal node details. DEPRECATED
>   baremetal unset  Unset baremetal properties. DEPRECATED
>   ca get         Retrieve a CA by providing its URI.
>   ca list        List cas.
>   catalog list   List services in the service catalog
>   catalog show   Display service catalog details
>   category create  Create a category.
>   category delete  Delete a category.
>   category list  List all available categories.
>   category show  Display category details.
>   claim create   Create claim and return a list of claimed messages
>   claim query    Display claim details
>   claim release  Delete a claim
>   claim renew    Renew a claim
>   class-schema   Show class schema.
>   command list   List recognized commands by group
>   complete       print bash completion command
>   compute agent create  Create compute agent
>   compute agent delete  Delete compute agent(s)
>   compute agent list  List compute agents
>   compute agent set  Set compute agent properties
>   compute service delete  Delete compute service(s)
>   compute service list  List compute services
>   compute service set  Set compute service properties
>   configuration show  Display configuration details
>   console log show  Show server's console output
>   console url show  Show server's remote console URL
>   container create  Create new container
>   container delete  Delete container
>   container list  List containers
>   container save  Save container contents locally
>   container set  Set container properties
>   container show  Display container details
>   container unset  Unset container properties
>   cron trigger create  Create new trigger.
>   cron trigger delete  Delete trigger.
>   cron trigger list  List all cron triggers.
>   cron trigger show  Show specific cron trigger.
>   dataprocessing cluster create  Creates cluster
>   dataprocessing cluster delete  Deletes cluster
>   dataprocessing cluster list  Lists clusters
>   dataprocessing cluster scale  Scales cluster
>   dataprocessing cluster show  Display cluster details
>   dataprocessing cluster template create  Creates cluster template
>   dataprocessing cluster template delete  Deletes cluster template
>   dataprocessing cluster template list  Lists cluster templates
>   dataprocessing cluster template show  Display cluster template details
>   dataprocessing cluster template update  Updates cluster template
>   dataprocessing cluster update  Updates cluster
>   dataprocessing cluster verification  Updates cluster verifications
>   dataprocessing data source create  Creates data source
>   dataprocessing data source delete  Delete data source
>   dataprocessing data source list  Lists data sources
>   dataprocessing data source show  Display data source details
>   dataprocessing data source update  Update data source
>   dataprocessing image list  Lists registered images
>   dataprocessing image register  Register an image
>   dataprocessing image show  Display image details
>   dataprocessing image tags add  Add image tags
>   dataprocessing image tags remove  Remove image tags
>   dataprocessing image tags set  Set image tags (Replace current image tags with provided ones)
>   dataprocessing image unregister  Unregister image(s)
>   dataprocessing job binary create  Creates job binary
>   dataprocessing job binary delete  Deletes job binary
>   dataprocessing job binary download  Downloads job binary
>   dataprocessing job binary list  Lists job binaries
>   dataprocessing job binary show  Display job binary details
>   dataprocessing job binary update  Updates job binary
>   dataprocessing job delete  Deletes job
>   dataprocessing job execute  Executes job
>   dataprocessing job list  Lists jobs
>   dataprocessing job show  Display job details
>   dataprocessing job template create  Creates job template
>   dataprocessing job template delete  Deletes job template
>   dataprocessing job template list  Lists job templates
>   dataprocessing job template show  Display job template details
>   dataprocessing job template update  Updates job template
>   dataprocessing job type configs get  Get job type configs
>   dataprocessing job type list  Lists job types supported by plugins
>   dataprocessing job update  Updates job
>   dataprocessing node group template create  Creates node group template
>   dataprocessing node group template delete  Deletes node group template
>   dataprocessing node group template list  Lists node group templates
>   dataprocessing node group template show  Display node group template details
>   dataprocessing node group template update  Updates node group template
>   dataprocessing plugin configs get  Get plugin configs
>   dataprocessing plugin list  Lists plugins
>   dataprocessing plugin show  Display plugin details
>   dataprocessing plugin update
>   deployment list  List deployments for an environment.
>   dns quota list  List quotas
>   dns quota reset  Delete blacklist
>   dns quota set  Set blacklist properties
>   dns service list  List service statuses
>   dns service show  Show service status details
>   ec2 credentials create  Create EC2 credentials
>   ec2 credentials delete  Delete EC2 credentials
>   ec2 credentials list  List EC2 credentials
>   ec2 credentials show  Display EC2 credentials details
>   endpoint create  Create new endpoint
>   endpoint delete  Delete endpoint(s)
>   endpoint list  List endpoints
>   endpoint show  Display endpoint details
>   environment apps edit  Edit environment's object model.
>   environment create  Create an environment.
>   environment delete  Delete an environment.
>   environment deploy  Start deployment of a murano environment session.
>   environment list  Lists environments
>   environment rename  Rename an environment.
>   environment session create  Creates a new configuration session for environment ID.
>   environment show  Display environment details
>   extension list  List API extensions
>   flavor create  Create new flavor
>   flavor delete  Delete flavor(s)
>   flavor list    List flavors
>   flavor set     Set flavor properties
>   flavor show    Display flavor details
>   flavor unset   Unset flavor properties
>   floating ip create  Create floating IP
>   floating ip delete  Delete floating IP(s)
>   floating ip list  List floating IP(s)
>   floating ip pool list  List pools of floating IP addresses
>   floating ip show  Display floating IP details
>   help           print detailed help for another command
>   host list      List hosts
>   host set       Set host properties
>   host show      Display host details
>   hypervisor list  List hypervisors
>   hypervisor show  Display hypervisor details
>   hypervisor stats show  Display hypervisor stats details
>   image add project  Associate project with image
>   image create   Create/upload an image
>   image delete   Delete image(s)
>   image list     List available images
>   image remove project  Disassociate project with image
>   image save     Save an image locally
>   image set      Set image properties
>   image show     Display image details
>   image unset    Unset image tags and properties
>   ip availability list  List IP availability for network
>   ip availability show  Show network IP availability details
>   keypair create  Create new public key
>   keypair delete  Delete public key(s)
>   keypair list   List public key fingerprints
>   keypair show   Display public key details
>   limits show    Show compute and block storage limits
>   messaging flavor create  Create a pool flavor
>   messaging flavor delete  Delete a flavor
>   messaging flavor list  List available flavors
>   messaging flavor show  Display flavor details
>   messaging flavor update  Update a flavor's attributes
>   messaging health  Display detailed health status of Zaqar server
>   messaging ping  Check if Zaqar server is alive or not
>   metric archive-policy create  Create an archive policy
>   metric archive-policy delete  Delete an archive policy
>   metric archive-policy list  List archive policies
>   metric archive-policy show  Show an archive policy
>   metric archive-policy-rule create  Create an archive policy rule
>   metric archive-policy-rule delete  Delete an archive policy rule
>   metric archive-policy-rule list  List archive policy rules
>   metric archive-policy-rule show  Show an archive policy rule
>   metric benchmark measures add  Do benchmark testing of adding measurements
>   metric benchmark measures show  Do benchmark testing of measurements show
>   metric benchmark metric create  Do benchmark testing of metric creation
>   metric benchmark metric show  Do benchmark testing of metric show
>   metric capabilities list  List capabilities
>   metric measures add  Add measurements to a metric
>   metric measures aggregation  Get measurements of aggregated metrics
>   metric measures batch-metrics
>   metric measures batch-resources-metrics
>   metric measures show  Get measurements of a metric
>   metric metric create  Create a metric
>   metric metric delete  Delete a metric
>   metric metric list  List metrics
>   metric metric show  Show a metric
>   metric resource batch delete  Delete a batch of resources based on attribute values
>   metric resource create  Create a resource
>   metric resource delete  Delete a resource
>   metric resource history  Show the history of a resource
>   metric resource list  List resources
>   metric resource search  Search resources with specified query rules
>   metric resource show  Show a resource
>   metric resource update  Update a resource
>   metric resource-type create  Create a resource type
>   metric resource-type delete  Delete a resource type
>   metric resource-type list  List resource types
>   metric resource-type show  Show a resource type
>   metric resource-type update
>   metric status  Show the status of measurements processing
>   module list    List module versions
>   network agent delete  Delete network agent(s)
>   network agent list  List network agents
>   network agent set  Set network agent properties
>   network agent show  Display network agent details
>   network create  Create new network
>   network delete  Delete network(s)
>   network list   List networks
>   network rbac create  Create network RBAC policy
>   network rbac delete  Delete network RBAC policy(s)
>   network rbac list  List network RBAC policies
>   network rbac set  Set network RBAC policy properties
>   network rbac show  Display network RBAC policy details
>   network segment list  List network segments
>   network segment show  Display network segment details
>   network set    Set network properties
>   network show   Show network details
>   network subport list  List all subports for a given network trunk
>   network trunk create  Create a network trunk for a given project
>   network trunk delete  Delete a given network trunk
>   network trunk list  List all network trunks
>   network trunk set  Set network trunk properties
>   network trunk show  Show information of a given network trunk
>   network trunk unset  Unset subports from a given network trunk
>   object create  Upload object to container
>   object delete  Delete object from container
>   object list    List objects
>   object save    Save object locally
>   object set     Set object properties
>   object show    Display object details
>   object store account set  Set account properties
>   object store account show  Display account details
>   object store account unset  Unset account properties
>   object unset   Unset object properties
>   orchestration build info  Retrieve build information.
>   orchestration resource type list  List resource types.
>   orchestration resource type show  Show details and optionally generate a template for a resource type.
>   orchestration service list  List the Heat engines.
>   orchestration template function list  List the available functions.
>   orchestration template validate  Validate a template
>   orchestration template version list  List the available template versions.
>   package create  Create an application package.
>   pool create    Create a pool
>   pool delete    Delete a pool
>   pool list      List available Pools
>   pool show      Display pool details
>   pool update    Update a pool attribute
>   port create    Create a new port
>   port delete    Delete port(s)
>   port list      List ports
>   port set       Set port properties
>   port show      Display port details
>   port unset     Unset port properties
>   project create  Create new project
>   project delete  Delete project(s)
>   project list   List projects
>   project set    Set project properties
>   project show   Display project details
>   project unset  Unset project properties
>   ptr record list  List floatingip ptr records
>   ptr record set  Set floatingip ptr record
>   ptr record show  Show floatingip ptr record details
>   ptr record unset  Unset floatingip ptr record
>   queue create   Create a queue
>   queue delete   Delete a queue
>   queue get metadata  Get queue metadata
>   queue list     List available queues
>   queue set metadata  Set queue metadata
>   queue signed url  Create a queue
>   queue stats    Get queue stats
>   quota set      Set quotas for project or class
>   quota show     Show quotas for project or class
>   recordset create  Create new recordset
>   recordset delete  Delete recordset
>   recordset list  List recordsets
>   recordset set  Set recordset properties
>   recordset show  Show recordset details
>   resource member create  Shares a resource to another tenant.
>   resource member delete  Delete a resource sharing relationship.
>   resource member list  List all members.
>   resource member show  Show specific member information.
>   resource member update  Update resource sharing status.
>   role add       Add role to project:user
>   role assignment list  List role assignments
>   role create    Create new role
>   role delete    Delete role(s)
>   role list      List roles
>   role remove    Remove role from project : user
>   role show      Display role details
>   router add port  Add a port to a router
>   router add subnet  Add a subnet to a router
>   router create  Create a new router
>   router delete  Delete router(s)
>   router list    List routers
>   router remove port  Remove a port from a router
>   router remove subnet  Remove a subnet from a router
>   router set     Set router properties
>   router show    Display router details
>   router unset   Unset router properties
>   secret container create  Store a container in Barbican.
>   secret container delete  Delete a container by providing its href.
>   secret container get  Retrieve a container by providing its URI.
>   secret container list  List containers.
>   secret delete  Delete a secret by providing its URI.
>   secret get     Retrieve a secret by providing its URI.
>   secret list    List secrets.
>   secret order create  Create a new order.
>   secret order delete  Delete an order by providing its href.
>   secret order get  Retrieve an order by providing its URI.
>   secret order list  List orders.
>   secret store   Store a secret in Barbican.
>   secret update  Update a secret with no payload in Barbican.
>   security group create  Create a new security group
>   security group delete  Delete security group(s)
>   security group list  List security groups
>   security group rule create  Create a new security group rule
>   security group rule delete  Delete security group rule(s)
>   security group rule list  List security group rules
>   security group rule show  Display security group rule details
>   security group set  Set security group properties
>   security group show  Display security group details
>   server add fixed ip  Add fixed IP address to server
>   server add floating ip  Add floating IP address to server
>   server add security group  Add security group to server
>   server add volume  Add volume to server
>   server backup create  Create a server backup image
>   server create  Create a new server
>   server delete  Delete server(s)
>   server dump create  Create a dump file in server(s)
>   server group create  Create a new server group.
>   server group delete  Delete existing server group(s).
>   server group list  List all server groups.
>   server group show  Display server group details.
>   server image create  Create a new server disk image from an existing server
>   server list    List servers
>   server lock    Lock server(s). A non-admin user will not be able to execute actions
>   server migrate  Migrate server to different host
>   server pause   Pause server(s)
>   server reboot  Perform a hard or soft server reboot
>   server rebuild  Rebuild server
>   server remove fixed ip  Remove fixed IP address from server
>   server remove floating ip  Remove floating IP address from server
>   server remove security group  Remove security group from server
>   server remove volume  Remove volume from server
>   server rescue  Put server in rescue mode
>   server resize  Scale server to a new flavor
>   server restore  Restore server(s)
>   server resume  Resume server(s)
>   server set     Set server properties
>   server shelve  Shelve server(s)
>   server show    Show server details
>   server ssh     SSH to server
>   server start   Start server(s).
>   server stop    Stop server(s).
>   server suspend  Suspend server(s)
>   server unlock  Unlock server(s)
>   server unpause  Unpause server(s)
>   server unrescue  Restore server from rescue mode
>   server unset   Unset server properties
>   server unshelve  Unshelve server(s)
>   service create  Create new service
>   service delete  Delete service(s)
>   service list   List services
>   service show   Display service details
>   snapshot create  Create new snapshot
>   snapshot delete  Delete volume snapshot(s)
>   snapshot list  List snapshots
>   snapshot set   Set snapshot properties
>   snapshot show  Display snapshot details
>   snapshot unset  Unset snapshot properties
>   software config create  Create software config
>   software config delete  Delete software configs
>   software config list  List software configs
>   software config show  Show software config details
>   software deployment create  Create a software deployment.
>   software deployment delete  Delete software deployment(s) and correlative config(s).
>   software deployment list  List software deployments.
>   software deployment metadata show  Get deployment configuration metadata for the specified server.
>   software deployment output show  Show a specific deployment output.
>   software deployment show  Show SoftwareDeployment Details.
>   stack abandon  Abandon stack and output results.
>   stack adopt    Adopt a stack.
>   stack cancel   Cancel current task for a stack.
>   stack check    Check a stack.
>   stack create   Create a stack.
>   stack delete   Delete stack(s).
>   stack environment show  Show a stack's environment.
>   stack event list  List events.
>   stack event show  Show event details.
>   stack failures list  Show information about failed stack resources.
>   stack file list  Show a stack's files map.
>   stack hook clear  Clear resource hooks on a given stack.
>   stack hook poll  List resources with pending hook for a stack.
>   stack list     List stacks.
>   stack output list  List stack outputs.
>   stack output show  Show stack output.
>   stack resource list  List stack resources.
>   stack resource mark unhealthy  Set resource's health.
>   stack resource metadata  Show resource metadata
>   stack resource show  Display stack resource.
>   stack resource signal  Signal a resource with optional data.
>   stack resume   Resume a stack.
>   stack show     Show stack details.
>   stack snapshot create  Create stack snapshot.
>   stack snapshot delete  Delete stack snapshot.
>   stack snapshot list  List stack snapshots.
>   stack snapshot restore  Restore stack snapshot
>   stack snapshot show  Show stack snapshot.
>   stack suspend  Suspend a stack.
>   stack template show  Display stack template.
>   stack update   Update a stack.
>   static-action call  Call static method of the MuranoPL class.
>   subnet create  Create a subnet
>   subnet delete  Delete subnet(s)
>   subnet list    List subnets
>   subnet pool create  Create subnet pool
>   subnet pool delete  Delete subnet pool(s)
>   subnet pool list  List subnet pools
>   subnet pool set  Set subnet pool properties
>   subnet pool show  Display subnet pool details
>   subnet pool unset  Unset subnet pool properties
>   subnet set     Set subnet properties
>   subnet show    Display subnet details
>   subnet unset   Unset subnet properties
>   subscription create  Create a subscription for queue
>   subscription delete  Delete a subscription
>   subscription list  List available subscriptions
>   subscription show  Display subscription details
>   subscription update  Update a subscription
>   task execution list  List all tasks.
>   task execution published show  Show task published variables.
>   task execution rerun  Rerun an existing task.
>   task execution result show  Show task output data.
>   task execution show  Show specific task.
>   tld create     Create new tld
>   tld delete     Delete tld
>   tld list       List tlds
>   tld set        Set tld properties
>   tld show       Show tld details
>   token issue    Issue new token
>   token revoke   Revoke existing token
>   usage list     List resource usage per project
>   usage show     Show resource usage for a single project
>   user create    Create new user
>   user delete    Delete user(s)
>   user list      List users
>   user role list  List user-role assignments
>   user set       Set user properties
>   user show      Display user details
>   volume backup create  Create new volume backup
>   volume backup delete  Delete volume backup(s)
>   volume backup list  List volume backups
>   volume backup restore  Restore volume backup
>   volume backup show  Display volume backup details
>   volume create  Create new volume
>   volume delete  Delete volume(s)
>   volume list    List volumes
>   volume qos associate  Associate a QoS specification to a volume type
>   volume qos create  Create new QoS specification
>   volume qos delete  Delete QoS specification
>   volume qos disassociate  Disassociate a QoS specification from a volume type
>   volume qos list  List QoS specifications
>   volume qos set  Set QoS specification properties
>   volume qos show  Display QoS specification details
>   volume qos unset  Unset QoS specification properties
>   volume service list  List service command
>   volume set     Set volume properties
>   volume show    Display volume details
>   volume transfer request list  Lists all volume transfer requests.
>   volume type create  Create new volume type
>   volume type delete  Delete volume type(s)
>   volume type list  List volume types
>   volume type set  Set volume type properties
>   volume type show  Display volume type details
>   volume type unset  Unset volume type properties
>   volume unset   Unset volume properties
>   workbook create  Create new workbook.
>   workbook definition show  Show workbook definition.
>   workbook delete  Delete workbook.
>   workbook list  List all workbooks.
>   workbook show  Show specific workbook.
>   workbook update  Update workbook.
>   workbook validate  Validate workbook.
>   workflow create  Create new workflow.
>   workflow definition show  Show workflow definition.
>   workflow delete  Delete workflow.
>   workflow engine service list  List all services.
>   workflow env create  Create new environment.
>   workflow env delete  Delete environment.
>   workflow env list  List all environments.
>   workflow env show  Show specific environment.
>   workflow env update  Update environment.
>   workflow execution create  Create new execution.
>   workflow execution delete  Delete execution.
>   workflow execution input show  Show execution input data.
>   workflow execution list  List all executions.
>   workflow execution output show  Show execution output data.
>   workflow execution show  Show specific execution.
>   workflow execution update  Update execution.
>   workflow list  List all workflows.
>   workflow show  Show specific workflow.
>   workflow update  Update workflow.
>   workflow validate  Validate workflow.
>   zone abandon   Abandon a zone
>   zone axfr      AXFR a zone
>   zone blacklist create  Create new blacklist
>   zone blacklist delete  Delete blacklist
>   zone blacklist list  List blacklists
>   zone blacklist set  Set blacklist properties
>   zone blacklist show  Show blacklist details
>   zone create    Create new zone
>   zone delete    Delete zone
>   zone export create  Export a Zone
>   zone export delete  Delete a Zone Export
>   zone export list  List Zone Exports
>   zone export show  Show a Zone Export
>   zone export showfile  Show the zone file for the Zone Export
>   zone import create  Import a Zone from a file on the filesystem
>   zone import delete  Delete a Zone Import
>   zone import list  List Zone Imports
>   zone import show  Show a Zone Import
>   zone list      List zones
>   zone set       Set zone properties
>   zone show      Show zone details
>   zone transfer accept list  List Zone Transfer Accepts
>   zone transfer accept request  Accept a Zone Transfer Request
>   zone transfer accept show  Show Zone Transfer Accept
>   zone transfer request create  Create new zone transfer request
>   zone transfer request delete  Delete a Zone Transfer Request
>   zone transfer request list  List Zone Transfer Requests
>   zone transfer request set  Set a Zone Transfer Request
>   zone transfer request show  Show Zone Transfer Request Details

  
---
layout: post
title: "[OpenStack] Command_Group"
description: " "
date: 2021-09-03
tags: [개발]
comments: true
share: true
---


### Command_Group 

+--------------------------------------+-------------------------------------------+
| Command Group                        | Commands                                  |
+--------------------------------------+-------------------------------------------+
| openstack.alarming.v2                | alarm create                              |
|                                      | alarm delete                              |
|                                      | alarm list                                |
|                                      | alarm show                                |
|                                      | alarm state get                           |
|                                      | alarm state set                           |
|                                      | alarm update                              |
|                                      | alarm-history search                      |
|                                      | alarm-history show                        |
|                                      | alarming capabilities list                |
| openstack.application_catalog.v1     | category create                           |
|                                      | category delete                           |
|                                      | category list                             |
|                                      | category show                             |
|                                      | class-schema                              |
|                                      | deployment list                           |
|                                      | environment apps edit                     |
|                                      | environment create                        |
|                                      | environment delete                        |
|                                      | environment deploy                        |
|                                      | environment list                          |
|                                      | environment rename                        |
|                                      | environment session create                |
|                                      | environment show                          |
|                                      | package create                            |
|                                      | static-action call                        |
| openstack.baremetal.v1               | baremetal chassis create                  |
|                                      | baremetal chassis delete                  |
|                                      | baremetal chassis list                    |
|                                      | baremetal chassis set                     |
|                                      | baremetal chassis show                    |
|                                      | baremetal chassis unset                   |
|                                      | baremetal create                          |
|                                      | baremetal delete                          |
|                                      | baremetal driver list                     |
|                                      | baremetal driver passthru call            |
|                                      | baremetal driver passthru list            |
|                                      | baremetal driver show                     |
|                                      | baremetal list                            |
|                                      | baremetal node abort                      |
|                                      | baremetal node adopt                      |
|                                      | baremetal node boot device set            |
|                                      | baremetal node boot device show           |
|                                      | baremetal node clean                      |
|                                      | baremetal node console disable            |
|                                      | baremetal node console enable             |
|                                      | baremetal node console show               |
|                                      | baremetal node create                     |
|                                      | baremetal node delete                     |
|                                      | baremetal node deploy                     |
|                                      | baremetal node inspect                    |
|                                      | baremetal node list                       |
|                                      | baremetal node maintenance set            |
|                                      | baremetal node maintenance unset          |
|                                      | baremetal node manage                     |
|                                      | baremetal node passthru call              |
|                                      | baremetal node passthru list              |
|                                      | baremetal node power                      |
|                                      | baremetal node provide                    |
|                                      | baremetal node reboot                     |
|                                      | baremetal node rebuild                    |
|                                      | baremetal node set                        |
|                                      | baremetal node show                       |
|                                      | baremetal node undeploy                   |
|                                      | baremetal node unset                      |
|                                      | baremetal node validate                   |
|                                      | baremetal port create                     |
|                                      | baremetal port delete                     |
|                                      | baremetal port list                       |
|                                      | baremetal port set                        |
|                                      | baremetal port show                       |
|                                      | baremetal port unset                      |
|                                      | baremetal set                             |
|                                      | baremetal show                            |
|                                      | baremetal unset                           |
| openstack.baremetal_introspection.v1 | baremetal introspection abort             |
|                                      | baremetal introspection data save         |
|                                      | baremetal introspection reprocess         |
|                                      | baremetal introspection rule delete       |
|                                      | baremetal introspection rule import       |
|                                      | baremetal introspection rule list         |
|                                      | baremetal introspection rule purge        |
|                                      | baremetal introspection rule show         |
|                                      | baremetal introspection start             |
|                                      | baremetal introspection status            |
| openstack.cli                        | command list                              |
|                                      | module list                               |
| openstack.common                     | availability zone list                    |
|                                      | configuration show                        |
|                                      | extension list                            |
|                                      | limits show                               |
|                                      | quota set                                 |
|                                      | quota show                                |
| openstack.compute.v2                 | aggregate add host                        |
|                                      | aggregate create                          |
|                                      | aggregate delete                          |
|                                      | aggregate list                            |
|                                      | aggregate remove host                     |
|                                      | aggregate set                             |
|                                      | aggregate show                            |
|                                      | aggregate unset                           |
|                                      | compute agent create                      |
|                                      | compute agent delete                      |
|                                      | compute agent list                        |
|                                      | compute agent set                         |
|                                      | compute service delete                    |
|                                      | compute service list                      |
|                                      | compute service set                       |
|                                      | console log show                          |
|                                      | console url show                          |
|                                      | flavor create                             |
|                                      | flavor delete                             |
|                                      | flavor list                               |
|                                      | flavor set                                |
|                                      | flavor show                               |
|                                      | flavor unset                              |
|                                      | host list                                 |
|                                      | host set                                  |
|                                      | host show                                 |
|                                      | hypervisor list                           |
|                                      | hypervisor show                           |
|                                      | hypervisor stats show                     |
|                                      | ip fixed add                              |
|                                      | ip fixed remove                           |
|                                      | ip floating add                           |
|                                      | ip floating remove                        |
|                                      | keypair create                            |
|                                      | keypair delete                            |
|                                      | keypair list                              |
|                                      | keypair show                              |
|                                      | server add fixed ip                       |
|                                      | server add floating ip                    |
|                                      | server add security group                 |
|                                      | server add volume                         |
|                                      | server backup create                      |
|                                      | server create                             |
|                                      | server delete                             |
|                                      | server dump create                        |
|                                      | server group create                       |
|                                      | server group delete                       |
|                                      | server group list                         |
|                                      | server group show                         |
|                                      | server image create                       |
|                                      | server list                               |
|                                      | server lock                               |
|                                      | server migrate                            |
|                                      | server pause                              |
|                                      | server reboot                             |
|                                      | server rebuild                            |
|                                      | server remove fixed ip                    |
|                                      | server remove floating ip                 |
|                                      | server remove security group              |
|                                      | server remove volume                      |
|                                      | server rescue                             |
|                                      | server resize                             |
|                                      | server restore                            |
|                                      | server resume                             |
|                                      | server set                                |
|                                      | server shelve                             |
|                                      | server show                               |
|                                      | server ssh                                |
|                                      | server start                              |
|                                      | server stop                               |
|                                      | server suspend                            |
|                                      | server unlock                             |
|                                      | server unpause                            |
|                                      | server unrescue                           |
|                                      | server unset                              |
|                                      | server unshelve                           |
|                                      | usage list                                |
|                                      | usage show                                |
| openstack.data_processing.v1         | dataprocessing cluster create             |
|                                      | dataprocessing cluster delete             |
|                                      | dataprocessing cluster list               |
|                                      | dataprocessing cluster scale              |
|                                      | dataprocessing cluster show               |
|                                      | dataprocessing cluster template create    |
|                                      | dataprocessing cluster template delete    |
|                                      | dataprocessing cluster template list      |
|                                      | dataprocessing cluster template show      |
|                                      | dataprocessing cluster template update    |
|                                      | dataprocessing cluster update             |
|                                      | dataprocessing cluster verification       |
|                                      | dataprocessing data source create         |
|                                      | dataprocessing data source delete         |
|                                      | dataprocessing data source list           |
|                                      | dataprocessing data source show           |
|                                      | dataprocessing data source update         |
|                                      | dataprocessing image list                 |
|                                      | dataprocessing image register             |
|                                      | dataprocessing image show                 |
|                                      | dataprocessing image tags add             |
|                                      | dataprocessing image tags remove          |
|                                      | dataprocessing image tags set             |
|                                      | dataprocessing image unregister           |
|                                      | dataprocessing job binary create          |
|                                      | dataprocessing job binary delete          |
|                                      | dataprocessing job binary download        |
|                                      | dataprocessing job binary list            |
|                                      | dataprocessing job binary show            |
|                                      | dataprocessing job binary update          |
|                                      | dataprocessing job delete                 |
|                                      | dataprocessing job execute                |
|                                      | dataprocessing job list                   |
|                                      | dataprocessing job show                   |
|                                      | dataprocessing job template create        |
|                                      | dataprocessing job template delete        |
|                                      | dataprocessing job template list          |
|                                      | dataprocessing job template show          |
|                                      | dataprocessing job template update        |
|                                      | dataprocessing job type configs get       |
|                                      | dataprocessing job type list              |
|                                      | dataprocessing job update                 |
|                                      | dataprocessing node group template create |
|                                      | dataprocessing node group template delete |
|                                      | dataprocessing node group template list   |
|                                      | dataprocessing node group template show   |
|                                      | dataprocessing node group template update |
|                                      | dataprocessing plugin configs get         |
|                                      | dataprocessing plugin list                |
|                                      | dataprocessing plugin show                |
|                                      | dataprocessing plugin update              |
| openstack.dns.v2                     | dns quota list                            |
|                                      | dns quota reset                           |
|                                      | dns quota set                             |
|                                      | dns service list                          |
|                                      | dns service show                          |
|                                      | ptr record list                           |
|                                      | ptr record set                            |
|                                      | ptr record show                           |
|                                      | ptr record unset                          |
|                                      | recordset create                          |
|                                      | recordset delete                          |
|                                      | recordset list                            |
|                                      | recordset set                             |
|                                      | recordset show                            |
|                                      | tld create                                |
|                                      | tld delete                                |
|                                      | tld list                                  |
|                                      | tld set                                   |
|                                      | tld show                                  |
|                                      | zone abandon                              |
|                                      | zone axfr                                 |
|                                      | zone blacklist create                     |
|                                      | zone blacklist delete                     |
|                                      | zone blacklist list                       |
|                                      | zone blacklist set                        |
|                                      | zone blacklist show                       |
|                                      | zone create                               |
|                                      | zone delete                               |
|                                      | zone export create                        |
|                                      | zone export delete                        |
|                                      | zone export list                          |
|                                      | zone export show                          |
|                                      | zone export showfile                      |
|                                      | zone import create                        |
|                                      | zone import delete                        |
|                                      | zone import list                          |
|                                      | zone import show                          |
|                                      | zone list                                 |
|                                      | zone set                                  |
|                                      | zone show                                 |
|                                      | zone transfer accept list                 |
|                                      | zone transfer accept request              |
|                                      | zone transfer accept show                 |
|                                      | zone transfer request create              |
|                                      | zone transfer request delete              |
|                                      | zone transfer request list                |
|                                      | zone transfer request set                 |
|                                      | zone transfer request show                |
| openstack.identity.v2                | catalog list                              |
|                                      | catalog show                              |
|                                      | ec2 credentials create                    |
|                                      | ec2 credentials delete                    |
|                                      | ec2 credentials list                      |
|                                      | ec2 credentials show                      |
|                                      | endpoint create                           |
|                                      | endpoint delete                           |
|                                      | endpoint list                             |
|                                      | endpoint show                             |
|                                      | project create                            |
|                                      | project delete                            |
|                                      | project list                              |
|                                      | project set                               |
|                                      | project show                              |
|                                      | project unset                             |
|                                      | role add                                  |
|                                      | role assignment list                      |
|                                      | role create                               |
|                                      | role delete                               |
|                                      | role list                                 |
|                                      | role remove                               |
|                                      | role show                                 |
|                                      | service create                            |
|                                      | service delete                            |
|                                      | service list                              |
|                                      | service show                              |
|                                      | token issue                               |
|                                      | token revoke                              |
|                                      | user create                               |
|                                      | user delete                               |
|                                      | user list                                 |
|                                      | user role list                            |
|                                      | user set                                  |
|                                      | user show                                 |
| openstack.image.v2                   | image add project                         |
|                                      | image create                              |
|                                      | image delete                              |
|                                      | image list                                |
|                                      | image remove project                      |
|                                      | image save                                |
|                                      | image set                                 |
|                                      | image show                                |
|                                      | image unset                               |
| openstack.key_manager.v1             | acl delete                                |
|                                      | acl get                                   |
|                                      | acl submit                                |
|                                      | acl user add                              |
|                                      | acl user remove                           |
|                                      | ca get                                    |
|                                      | ca list                                   |
|                                      | secret container create                   |
|                                      | secret container delete                   |
|                                      | secret container get                      |
|                                      | secret container list                     |
|                                      | secret delete                             |
|                                      | secret get                                |
|                                      | secret list                               |
|                                      | secret order create                       |
|                                      | secret order delete                       |
|                                      | secret order get                          |
|                                      | secret order list                         |
|                                      | secret store                              |
|                                      | secret update                             |
| openstack.messaging.v2               | claim create                              |
|                                      | claim query                               |
|                                      | claim release                             |
|                                      | claim renew                               |
|                                      | messaging flavor create                   |
|                                      | messaging flavor delete                   |
|                                      | messaging flavor list                     |
|                                      | messaging flavor show                     |
|                                      | messaging flavor update                   |
|                                      | messaging health                          |
|                                      | messaging ping                            |
|                                      | pool create                               |
|                                      | pool delete                               |
|                                      | pool list                                 |
|                                      | pool show                                 |
|                                      | pool update                               |
|                                      | queue create                              |
|                                      | queue delete                              |
|                                      | queue get metadata                        |
|                                      | queue list                                |
|                                      | queue set metadata                        |
|                                      | queue signed url                          |
|                                      | queue stats                               |
|                                      | subscription create                       |
|                                      | subscription delete                       |
|                                      | subscription list                         |
|                                      | subscription show                         |
|                                      | subscription update                       |
| openstack.metric.v1                  | metric archive-policy create              |
|                                      | metric archive-policy delete              |
|                                      | metric archive-policy list                |
|                                      | metric archive-policy show                |
|                                      | metric archive-policy-rule create         |
|                                      | metric archive-policy-rule delete         |
|                                      | metric archive-policy-rule list           |
|                                      | metric archive-policy-rule show           |
|                                      | metric benchmark measures add             |
|                                      | metric benchmark measures show            |
|                                      | metric benchmark metric create            |
|                                      | metric benchmark metric show              |
|                                      | metric capabilities list                  |
|                                      | metric measures add                       |
|                                      | metric measures aggregation               |
|                                      | metric measures batch-metrics             |
|                                      | metric measures batch-resources-metrics   |
|                                      | metric measures show                      |
|                                      | metric metric create                      |
|                                      | metric metric delete                      |
|                                      | metric metric list                        |
|                                      | metric metric show                        |
|                                      | metric resource batch delete              |
|                                      | metric resource create                    |
|                                      | metric resource delete                    |
|                                      | metric resource history                   |
|                                      | metric resource list                      |
|                                      | metric resource search                    |
|                                      | metric resource show                      |
|                                      | metric resource update                    |
|                                      | metric resource-type create               |
|                                      | metric resource-type delete               |
|                                      | metric resource-type list                 |
|                                      | metric resource-type show                 |
|                                      | metric resource-type update               |
|                                      | metric status                             |
| openstack.network.v2                 | address scope create                      |
|                                      | address scope delete                      |
|                                      | address scope list                        |
|                                      | address scope set                         |
|                                      | address scope show                        |
|                                      | floating ip create                        |
|                                      | floating ip delete                        |
|                                      | floating ip list                          |
|                                      | floating ip pool list                     |
|                                      | floating ip show                          |
|                                      | ip availability list                      |
|                                      | ip availability show                      |
|                                      | ip floating create                        |
|                                      | ip floating delete                        |
|                                      | ip floating list                          |
|                                      | ip floating pool list                     |
|                                      | ip floating show                          |
|                                      | network agent delete                      |
|                                      | network agent list                        |
|                                      | network agent set                         |
|                                      | network agent show                        |
|                                      | network create                            |
|                                      | network delete                            |
|                                      | network list                              |
|                                      | network rbac create                       |
|                                      | network rbac delete                       |
|                                      | network rbac list                         |
|                                      | network rbac set                          |
|                                      | network rbac show                         |
|                                      | network segment list                      |
|                                      | network segment show                      |
|                                      | network set                               |
|                                      | network show                              |
|                                      | port create                               |
|                                      | port delete                               |
|                                      | port list                                 |
|                                      | port set                                  |
|                                      | port show                                 |
|                                      | port unset                                |
|                                      | router add port                           |
|                                      | router add subnet                         |
|                                      | router create                             |
|                                      | router delete                             |
|                                      | router list                               |
|                                      | router remove port                        |
|                                      | router remove subnet                      |
|                                      | router set                                |
|                                      | router show                               |
|                                      | router unset                              |
|                                      | security group create                     |
|                                      | security group delete                     |
|                                      | security group list                       |
|                                      | security group rule create                |
|                                      | security group rule delete                |
|                                      | security group rule list                  |
|                                      | security group rule show                  |
|                                      | security group set                        |
|                                      | security group show                       |
|                                      | subnet create                             |
|                                      | subnet delete                             |
|                                      | subnet list                               |
|                                      | subnet pool create                        |
|                                      | subnet pool delete                        |
|                                      | subnet pool list                          |
|                                      | subnet pool set                           |
|                                      | subnet pool show                          |
|                                      | subnet pool unset                         |
|                                      | subnet set                                |
|                                      | subnet show                               |
|                                      | subnet unset                              |
| openstack.neutronclient.v2           | network subport list                      |
|                                      | network trunk create                      |
|                                      | network trunk delete                      |
|                                      | network trunk list                        |
|                                      | network trunk set                         |
|                                      | network trunk show                        |
|                                      | network trunk unset                       |
| openstack.object_store.v1            | container create                          |
|                                      | container delete                          |
|                                      | container list                            |
|                                      | container save                            |
|                                      | container set                             |
|                                      | container show                            |
|                                      | container unset                           |
|                                      | object create                             |
|                                      | object delete                             |
|                                      | object list                               |
|                                      | object save                               |
|                                      | object set                                |
|                                      | object show                               |
|                                      | object store account set                  |
|                                      | object store account show                 |
|                                      | object store account unset                |
|                                      | object unset                              |
| openstack.orchestration.v1           | orchestration build info                  |
|                                      | orchestration resource type list          |
|                                      | orchestration resource type show          |
|                                      | orchestration service list                |
|                                      | orchestration template function list      |
|                                      | orchestration template validate           |
|                                      | orchestration template version list       |
|                                      | software config create                    |
|                                      | software config delete                    |
|                                      | software config list                      |
|                                      | software config show                      |
|                                      | software deployment create                |
|                                      | software deployment delete                |
|                                      | software deployment list                  |
|                                      | software deployment metadata show         |
|                                      | software deployment output show           |
|                                      | software deployment show                  |
|                                      | stack abandon                             |
|                                      | stack adopt                               |
|                                      | stack cancel                              |
|                                      | stack check                               |
|                                      | stack create                              |
|                                      | stack delete                              |
|                                      | stack environment show                    |
|                                      | stack event list                          |
|                                      | stack event show                          |
|                                      | stack failures list                       |
|                                      | stack file list                           |
|                                      | stack hook clear                          |
|                                      | stack hook poll                           |
|                                      | stack list                                |
|                                      | stack output list                         |
|                                      | stack output show                         |
|                                      | stack resource list                       |
|                                      | stack resource mark unhealthy             |
|                                      | stack resource metadata                   |
|                                      | stack resource show                       |
|                                      | stack resource signal                     |
|                                      | stack resume                              |
|                                      | stack show                                |
|                                      | stack snapshot create                     |
|                                      | stack snapshot delete                     |
|                                      | stack snapshot list                       |
|                                      | stack snapshot restore                    |
|                                      | stack snapshot show                       |
|                                      | stack suspend                             |
|                                      | stack template show                       |
|                                      | stack update                              |
| openstack.volume.v2                  | backup create                             |
|                                      | backup delete                             |
|                                      | backup list                               |
|                                      | backup restore                            |
|                                      | backup show                               |
|                                      | snapshot create                           |
|                                      | snapshot delete                           |
|                                      | snapshot list                             |
|                                      | snapshot set                              |
|                                      | snapshot show                             |
|                                      | snapshot unset                            |
|                                      | volume backup create                      |
|                                      | volume backup delete                      |
|                                      | volume backup list                        |
|                                      | volume backup restore                     |
|                                      | volume backup show                        |
|                                      | volume create                             |
|                                      | volume delete                             |
|                                      | volume list                               |
|                                      | volume qos associate                      |
|                                      | volume qos create                         |
|                                      | volume qos delete                         |
|                                      | volume qos disassociate                   |
|                                      | volume qos list                           |
|                                      | volume qos set                            |
|                                      | volume qos show                           |
|                                      | volume qos unset                          |
|                                      | volume service list                       |
|                                      | volume set                                |
|                                      | volume show                               |
|                                      | volume transfer request list              |
|                                      | volume type create                        |
|                                      | volume type delete                        |
|                                      | volume type list                          |
|                                      | volume type set                           |
|                                      | volume type show                          |
|                                      | volume type unset                         |
|                                      | volume unset                              |
| openstack.workflow_engine.v2         | action definition create                  |
|                                      | action definition definition show         |
|                                      | action definition delete                  |
|                                      | action definition list                    |
|                                      | action definition show                    |
|                                      | action definition update                  |
|                                      | action execution delete                   |
|                                      | action execution input show               |
|                                      | action execution list                  7   |
|                                      | action execution output show              |
|                                      | action execution run                      |
|                                      | action execution show                     |
|                                      | action execution update                   |
|                                      | cron trigger create                       |
|                                      | cron trigger delete                       |
|                                      | cron trigger list                         |
|                                      | cron trigger show                         |
|                                      | resource member create                    |
|                                      | resource member delete                    |
|                                      | resource member list                      |
|                                      | resource member show                      |
|                                      | resource member update                    |
|                                      | task execution list                       |
|                                      | task execution published show             |
|                                      | task execution rerun                      |
|                                      | task execution result show                |
|                                      | task execution show                       |
|                                      | workbook create                           |
|                                      | workbook definition show                  |
|                                      | workbook delete                           |
|                                      | workbook list                             |
|                                      | workbook show                             |
|                                      | workbook update                           |
|                                      | workbook validate                         |
|                                      | workflow create                           |
|                                      | workflow definition show                  |
|                                      | workflow delete                           |
|                                      | workflow engine service list              |
|                                      | workflow env create                       |
|                                      | workflow env delete                       |
|                                      | workflow env list                         |
|                                      | workflow env show                         |
|                                      | workflow env update                       |
|                                      | workflow execution create                 |
|                                      | workflow execution delete                 |
|                                      | workflow execution input show             |
|                                      | workflow execution list                   |
|                                      | workflow execution output show            |
|                                      | workflow execution show                   |
|                                      | workflow execution update                 |
|                                      | workflow list                             |
|                                      | workflow show                             |
|                                      | workflow update                           |
|                                      | workflow validate                         |
+--------------------------------------+-------------------------------------------+
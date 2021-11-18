---
layout: post
title: "[Symfony] Customize with Symfony"
description: " "
date: 2021-11-18
tags: [Symfony]
comments: true
share: true
---

Customize with Symfony
--------
[EC-CUBE4 Document][a]

[a]:https://doc4.ec-cube.net/customize_symfony
[Event Dispatcher (Symfony)][b]

[b]:https://symfony.com/doc/current/event_dispatcher.html

### Symfony Event

~~~~~php
<?php

namespace Customize\EventListener;

use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpKernel\Event\FilterResponseEvent;
use Symfony\Component\HttpKernel\KernelEvents;

class HelloListener implements EventSubscriberInterface
{
    public function onResponse(FilterResponseEvent $event)
    {
        echo 'hello world';　// Method 詳細
    }

    public static function getSubscribedEvents()
    {
        return [
            KernelEvents::RESPONSE => 'onResponse', // Event名・Method 追加
        ];
    }
}
~~~~~

 ### Use Entity Manager in Listener

[Ref][s]

[s]:https://stackoverflow.com/questions/27392739/symfony2-how-to-get-entity-manager-in-listener
 ~~~~php

namespace MPN\CRMBundle\Manager;

use Doctrine\ORM\EntityManager;
use MPN\CRMBundle\Entity\Analytics;
use MPN\CRMBundle\Service\DateTimeBuilder;

class AnalyticsManager
{
    /**
     * @var EntityManager
     */
    public $em;

    /**
     * @var DateTimeBuilder
     */
    private $dateTimeBuilder;

    /**
     * @var array
     */
    private $analytics;

    public function __construct(EntityManager $em, DateTimeBuilder $dateTimeBuilder)
    {
        $this->em = $em;　 // EntityManager
        $this->dateTimeBuilder = $dateTimeBuilder;
        $this->setup();
    }

    /**
     * Flushes the data to the database.
     *
     * @return void
     */
    public function save()
    {
        $this->em->flush();  // 保存
    }
}

 ~~~~

### Render in Listener

[EC-CUBE4 Event Listener][e]

[e]:https://github.com/EC-CUBE/ec-cube/blob/4.0/src/Eccube/EventListener/TwigInitializeListener.php
[Ref][re]

[re]:https://stackoverflow.com/questions/6874521/how-to-render-a-template-inside-an-eventlistener
~~~~php
use Twig\Environment;

public $_engine;

public function __construct(\Swift_Mailer $mailer, Environment $engine)
{
    $this->mailer= $mailer;
    $this->_engine = $engine;
}

this->mailer->send( (new \Swift_Message('something happened'))
            ->setFrom('test@test.com')
            ->setTo('user@user.com')
            ->setBody($this->_engine->render('mails/test.html.twig',[
             ])
        );
~~~~
~~~~php
use Twig\Environment;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

class TwigInitializeListener implements EventSubscriberInterface
{
/**
    * @var Environment
    */
   protected $twig;
   /**
       * TwigInitializeListener constructor.
       *
       * @param Environment $twig
       */
      public function __construct(
          Environment $twig,
      ) {
          $this->twig = $twig;
      }

~~~~
* send var to view from event listener 
~~~~php
$this->twig->addGlobal('Page', $Page);

$this->twig->render(
                  　  'Entry/confirm.twig',
                  　  [
                      'form' => $form->createView(),
                  　  ]
                  　);
~~~~

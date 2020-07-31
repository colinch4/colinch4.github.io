## RPM-GPG-KEY

- **rpm-build를 위한 GPG Key 생성**

1. 사전작업
   - rpm 빌드용 계정 생성 (root가 아닌 계정이 권장됨)

2. gpg-agent 시작

   ```shell
   $ rngd -r /dev/urandom
   $ gpg-agent --use-standard-socket --daemon
   ```

3. Key 생성

   - 명령어 예시

     ```shell
     $ cat <<EOF | gpg2 --batch --no-tty --gen-key
     %echo Generating a standard key
     Key-Type: default
     Key-Length: 2048
     Subkey-Type: default
     Subkey-Length: 2048
     Name-Real: Jmnote
     Name-Email: jmnote@example.com
     Expire-Date: 10y
     Passphrase: P@ssw0rd
     %commit
     %echo done
     EOF
     ```

     - Name-Real(실명), Name-Email(이메일), Expire-Date(만료일 - 0으로 하면 만료되지 않는다. 여기서는 10y로 했으므로 10년 후 만료), Passphrase(암호)를 적절히 입력
     - 이 명령어 실행은 몇 초 이내에 끝난다. 만약 끝나지 않고 있으면 `Ctrl+C`로 취소하고 root계정으로 "gpg-agent 시작" 문단내용을 수행한 후에 다시 해보자.

4. gpg 지문 확인

   ```shell
   $ gpg --fingerprint
   ```

   > ```shell
   > [builduser@jmnote ~]$ gpg --fingerprint
   > gpg: checking the trustdb
   > gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
   > gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
   > gpg: next trustdb check due at 2024-05-29
   > /home/builduser/.gnupg/pubring.gpg
   > ----------------------------------
   > pub   2048R/8E933200 2014-06-01 [expires: 2024-05-29]
   >       Key fingerprint = 2EF8 4B50 BD83 AFAE 3A75  A2DB FD67 3C78 8E93 3200
   > uid                  Jmnote <jmnote@example.com>
   > sub   2048R/3D2F8AC9 2014-06-01 [expires: 2024-05-29]
   > ```
   >
   > 키 8E933200 는 여기서도 확인할 수 있다. 다음 과정에서 이 값이 필요하다.

5. 키 파일 추출

   ```shell
   $ gpg -a -o RPM-GPG-KEY-builduser --export 8E933200
   $ cat RPM-GPG-KEY-builduser 
   ```

   ```shell
   $ echo '%_gpg_name 8E933200' > ~/.rpmmacros
   $ cat ~/.rpmmacros
   ```

   
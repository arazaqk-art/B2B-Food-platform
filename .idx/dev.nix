{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # Or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.django
    pkgs.python311Packages.djangorestframework
    pkgs.python311Packages.celery
    pkgs.python311Packages.redis
  ];
  # Sets environment variables in the workspace
  env = {};
  # Fast way to run commands on instance startup
  startup = {
    # Add commands here to run on instance startup.
  };
}
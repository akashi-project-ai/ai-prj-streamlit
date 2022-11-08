git checkout -- .
git clean -f
git pull
yarn --production=false
yarn storybook:build